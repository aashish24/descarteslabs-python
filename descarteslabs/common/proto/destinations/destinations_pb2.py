# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: descarteslabs/common/proto/destinations/destinations.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='descarteslabs/common/proto/destinations/destinations.proto',
  package='descarteslabs.workflows',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n:descarteslabs/common/proto/destinations/destinations.proto\x12\x17\x64\x65scarteslabs.workflows\"\xc2\x01\n\x0b\x44\x65stination\x12=\n\x08\x64ownload\x18\x01 \x01(\x0b\x32!.descarteslabs.workflows.DownloadR\x08\x64ownload\x12\x34\n\x05\x65mail\x18\x02 \x01(\x0b\x32\x1e.descarteslabs.workflows.EmailR\x05\x65mail\x12!\n\x0chas_download\x18\x14 \x01(\x08R\x0bhasDownload\x12\x1b\n\thas_email\x18\x15 \x01(\x08R\x08hasEmail\"\n\n\x08\x44ownload\"5\n\x05\x45mail\x12\x18\n\x07subject\x18\x01 \x01(\tR\x07subject\x12\x12\n\x04\x62ody\x18\x02 \x01(\tR\x04\x62odyb\x06proto3'
)




_DESTINATION = _descriptor.Descriptor(
  name='Destination',
  full_name='descarteslabs.workflows.Destination',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='download', full_name='descarteslabs.workflows.Destination.download', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='download', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='descarteslabs.workflows.Destination.email', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='email', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_download', full_name='descarteslabs.workflows.Destination.has_download', index=2,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hasDownload', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_email', full_name='descarteslabs.workflows.Destination.has_email', index=3,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hasEmail', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=282,
)


_DOWNLOAD = _descriptor.Descriptor(
  name='Download',
  full_name='descarteslabs.workflows.Download',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=284,
  serialized_end=294,
)


_EMAIL = _descriptor.Descriptor(
  name='Email',
  full_name='descarteslabs.workflows.Email',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subject', full_name='descarteslabs.workflows.Email.subject', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='subject', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='descarteslabs.workflows.Email.body', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='body', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=296,
  serialized_end=349,
)

_DESTINATION.fields_by_name['download'].message_type = _DOWNLOAD
_DESTINATION.fields_by_name['email'].message_type = _EMAIL
DESCRIPTOR.message_types_by_name['Destination'] = _DESTINATION
DESCRIPTOR.message_types_by_name['Download'] = _DOWNLOAD
DESCRIPTOR.message_types_by_name['Email'] = _EMAIL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Destination = _reflection.GeneratedProtocolMessageType('Destination', (_message.Message,), {
  'DESCRIPTOR' : _DESTINATION,
  '__module__' : 'descarteslabs.common.proto.destinations.destinations_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Destination)
  })
_sym_db.RegisterMessage(Destination)

Download = _reflection.GeneratedProtocolMessageType('Download', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOAD,
  '__module__' : 'descarteslabs.common.proto.destinations.destinations_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Download)
  })
_sym_db.RegisterMessage(Download)

Email = _reflection.GeneratedProtocolMessageType('Email', (_message.Message,), {
  'DESCRIPTOR' : _EMAIL,
  '__module__' : 'descarteslabs.common.proto.destinations.destinations_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Email)
  })
_sym_db.RegisterMessage(Email)


# @@protoc_insertion_point(module_scope)
