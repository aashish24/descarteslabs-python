import os
from collections import OrderedDict

import certifi
import grpc
from descarteslabs.client.auth import Auth
from descarteslabs.common.proto.health import health_pb2, health_pb2_grpc
from descarteslabs.common.retry import Retry, RetryError
from descarteslabs.common.retry.retry import _wraps


from .exceptions import from_grpc_error
from .auth import TokenProviderMetadataPlugin


_RETRYABLE_STATUS_CODES = {
    grpc.StatusCode.UNAVAILABLE,
    grpc.StatusCode.INTERNAL,
    grpc.StatusCode.RESOURCE_EXHAUSTED,
    grpc.StatusCode.UNKNOWN,
    grpc.StatusCode.DEADLINE_EXCEEDED,
}


def wrap_stub(func, default_retry, default_metadata=None):
    if default_metadata is None:
        default_metadata = tuple()

    @_wraps(func)
    def wrapper(*args, **kwargs):
        retry = kwargs.pop("retry", default_retry)

        # If retry is none, use identity function.
        if retry is None:

            def retry(f):
                return f

        # Merge and set default request headers
        # example: https://github.com/grpc/grpc/blob/master/examples/python/metadata/metadata_client.py
        # NOTE(Clark): We use an OrderedDict to ensure a stable ordering for Python 3.5
        # and 3.6.
        # TODO(Clark): Revert back to dict once Python 3.5 is dropped.
        merged_metadata = OrderedDict(
            default_metadata + kwargs.get("metadata", tuple())
        )

        kwargs["metadata"] = tuple(merged_metadata.items())

        try:
            return retry(func)(*args, **kwargs)
        except grpc.RpcError as e:
            raise from_grpc_error(e) from None
        except RetryError as e:
            e._exceptions = [
                from_grpc_error(exc) if isinstance(exc, grpc.RpcError) else exc
                for exc in e._exceptions
            ]
            raise e from e._exceptions[-1]

    return wrapper


def default_grpc_retry_predicate(e):
    try:
        code = e.code()
    except AttributeError:
        return False
    else:
        return code in _RETRYABLE_STATUS_CODES


class GrpcClient:
    """Low-level gRPC client for interacting with the gRPC backends.
    Not intended for users to use directly.

    Examples
    --------
    >>> from descarteslabs.client.grpc import GrpcClient
    >>> class MyClient(GrpcClient):
    ...     def __init__(self):
    ...         # derived classes should configure host
    ...         super().__init__("localhost")
    ...     def _populate_api(self):
    ...         # derived classes must add stubs and RPC methods
    ...         pass
    >>> client = MyClient()
    """

    DEFAULT_TIMEOUT = 5
    STREAM_TIMEOUT = 60 * 60 * 24

    def __init__(
        self,
        host,
        auth=None,
        certificate=None,
        port=443,
        default_retry=None,
        default_metadata=None,
    ):
        if auth is None:
            auth = Auth()

        self.auth = auth
        self.host = host
        self.port = port

        self._default_metadata = default_metadata
        if default_retry is None:
            default_retry = Retry(predicate=default_grpc_retry_predicate, retries=5)
        self._default_retry = default_retry

        self._channel = None
        self._certificate = certificate
        self._stubs = None
        self._api = None

    @property
    def token(self):
        "The Client token."
        return self.auth.token

    @property
    def channel(self):
        "The GRPC channel of the Client."
        if self._channel is None:
            self._channel = self._open_channel()
        return self._channel

    @property
    def certificate(self):
        "The Client SSL certificate."
        if self._certificate is None:
            cert_file = os.getenv("SSL_CERT_FILE", certifi.where())
            with open(cert_file, "rb") as f:
                self._certificate = f.read()

        return self._certificate

    @property
    def api(self):
        "The available Client operations, as a dict."
        if self._api is None:
            self._initialize()
        return self._api

    def _add_stub(self, name, stub):
        self._stubs[name] = stub(self.channel)

    def _add_api(self, stub_name, func_name, default_retry=None):
        stub = self._stubs[stub_name]
        func = getattr(stub, func_name)

        self._api[func_name] = wrap_stub(
            func, default_retry=default_retry, default_metadata=self._default_metadata
        )

    def _initialize(self):
        self._stubs = {}
        self._add_stub("Health", health_pb2_grpc.HealthStub)

        self._api = {}
        self._add_api("Health", "Check")
        self._populate_api()

    def _populate_api(self):
        """Derived gRPC client classes should use this method to add stubs and RPC methods."""
        raise NotImplementedError

    def _get_credentials(self):
        token_provider_plugin = TokenProviderMetadataPlugin(
            # NOTE: This property accessor will fetch a new token if need be.
            lambda: self.token
        )
        dl_auth_call_credentials = grpc.metadata_call_credentials(
            token_provider_plugin, "DL auth plugin"
        )
        ssl_channel_credentials = grpc.ssl_channel_credentials(self.certificate)

        composite_credentials = grpc.composite_channel_credentials(
            ssl_channel_credentials, dl_auth_call_credentials
        )

        return composite_credentials

    def _open_channel(self):
        return grpc.secure_channel(
            "{}:{}".format(self.host, self.port), self._get_credentials()
        )

    def health(self, timeout=None):
        """Check the health of the GRPC server (SERVING, NOT_SERVING, UNKNOWN).

        Example
        -------
        >>> from descarteslabs.client.grpc import GrpcClient
        >>> GrpcClient().health() # doctest: +SKIP
        SERVING
        """
        if timeout is None:
            timeout = self.DEFAULT_TIMEOUT

        return self.api["Check"](
            health_pb2.HealthCheckRequest(), timeout=self.DEFAULT_TIMEOUT
        )

    def close(self):
        "Close the GRPC channel associated with the Client."
        # NOTE: this may be a blocking operation
        if self._channel:
            self._channel.close()
            self._channel = None

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.close()

    def __del__(self):
        self.close()
