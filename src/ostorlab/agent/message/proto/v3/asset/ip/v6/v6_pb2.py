# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ostorlab/agent/message/proto/v3/asset/ip/v6/v6.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ostorlab/agent/message/proto/v3/asset/ip/v6/v6.proto',
  package='ostorlab.agent.message.proto.v3.asset.ip.v6',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n4ostorlab/agent/message/proto/v3/asset/ip/v6/v6.proto\x12+ostorlab.agent.message.proto.v3.asset.ip.v6\"9\n\x07Message\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04mask\x18\x02 \x01(\t\x12\x12\n\x07version\x18\x03 \x01(\x05:\x01\x36')
)




_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.Message.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mask', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.Message.mask', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.Message.version', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=6,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=158,
)

DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'ostorlab.agent.message.proto.v3.asset.ip.v6.v6_pb2'
  # @@protoc_insertion_point(class_scope:ostorlab.agent.message.proto.v3.asset.ip.v6.Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
