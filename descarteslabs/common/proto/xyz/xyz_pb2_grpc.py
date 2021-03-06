# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from descarteslabs.common.proto.xyz import xyz_pb2 as descarteslabs_dot_common_dot_proto_dot_xyz_dot_xyz__pb2


class XYZAPIStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateXYZ = channel.unary_unary(
        '/descarteslabs.workflows.XYZAPI/CreateXYZ',
        request_serializer=descarteslabs_dot_common_dot_proto_dot_xyz_dot_xyz__pb2.CreateXYZRequest.SerializeToString,
        response_deserializer=descarteslabs_dot_common_dot_proto_dot_xyz_dot_xyz__pb2.XYZ.FromString,
        )
    self.GetXYZ = channel.unary_unary(
        '/descarteslabs.workflows.XYZAPI/GetXYZ',
        request_serializer=descarteslabs_dot_common_dot_proto_dot_xyz_dot_xyz__pb2.GetXYZRequest.SerializeToString,
        response_deserializer=descarteslabs_dot_common_dot_proto_dot_xyz_dot_xyz__pb2.XYZ.FromString,
        )
    self.GetXYZSessionErrors = channel.unary_stream(
        '/descarteslabs.workflows.XYZAPI/GetXYZSessionErrors',
        request_serializer=descarteslabs_dot_common_dot_proto_dot_xyz_dot_xyz__pb2.GetXYZSessionErrorsRequest.SerializeToString,
        response_deserializer=descarteslabs_dot_common_dot_proto_dot_xyz_dot_xyz__pb2.XYZError.FromString,
        )


class XYZAPIServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateXYZ(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetXYZ(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetXYZSessionErrors(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_XYZAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateXYZ': grpc.unary_unary_rpc_method_handler(
          servicer.CreateXYZ,
          request_deserializer=descarteslabs_dot_common_dot_proto_dot_xyz_dot_xyz__pb2.CreateXYZRequest.FromString,
          response_serializer=descarteslabs_dot_common_dot_proto_dot_xyz_dot_xyz__pb2.XYZ.SerializeToString,
      ),
      'GetXYZ': grpc.unary_unary_rpc_method_handler(
          servicer.GetXYZ,
          request_deserializer=descarteslabs_dot_common_dot_proto_dot_xyz_dot_xyz__pb2.GetXYZRequest.FromString,
          response_serializer=descarteslabs_dot_common_dot_proto_dot_xyz_dot_xyz__pb2.XYZ.SerializeToString,
      ),
      'GetXYZSessionErrors': grpc.unary_stream_rpc_method_handler(
          servicer.GetXYZSessionErrors,
          request_deserializer=descarteslabs_dot_common_dot_proto_dot_xyz_dot_xyz__pb2.GetXYZSessionErrorsRequest.FromString,
          response_serializer=descarteslabs_dot_common_dot_proto_dot_xyz_dot_xyz__pb2.XYZError.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'descarteslabs.workflows.XYZAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
