# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ostorlab/agent/message/proto/v3/fingerprint/domain_name/service/x509/x509.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ostorlab.agent.message.proto.common.x509 import x509_pb2 as ostorlab_dot_agent_dot_message_dot_proto_dot_common_dot_x509_dot_x509__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ostorlab/agent/message/proto/v3/fingerprint/domain_name/service/x509/x509.proto',
  package='ostorlab.agent.message.proto.v3.fingerprint.domain_name.service.x509',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\nOostorlab/agent/message/proto/v3/fingerprint/domain_name/service/x509/x509.proto\x12\x44ostorlab.agent.message.proto.v3.fingerprint.domain_name.service.x509\x1a\x33ostorlab/agent/message/proto/common/x509/x509.proto\"}\n\x07Message\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x0e\n\x06schema\x18\x03 \x01(\t\x12\x46\n\ncert_chain\x18\x04 \x03(\x0b\x32\x32.ostorlab.agent.message.proto.common.x509.X509Cert')
  ,
  dependencies=[ostorlab_dot_agent_dot_message_dot_proto_dot_common_dot_x509_dot_x509__pb2.DESCRIPTOR,])




_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='ostorlab.agent.message.proto.v3.fingerprint.domain_name.service.x509.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ostorlab.agent.message.proto.v3.fingerprint.domain_name.service.x509.Message.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='ostorlab.agent.message.proto.v3.fingerprint.domain_name.service.x509.Message.port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schema', full_name='ostorlab.agent.message.proto.v3.fingerprint.domain_name.service.x509.Message.schema', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cert_chain', full_name='ostorlab.agent.message.proto.v3.fingerprint.domain_name.service.x509.Message.cert_chain', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=206,
  serialized_end=331,
)

_MESSAGE.fields_by_name['cert_chain'].message_type = ostorlab_dot_agent_dot_message_dot_proto_dot_common_dot_x509_dot_x509__pb2._X509CERT
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'ostorlab.agent.message.proto.v3.fingerprint.domain_name.service.x509.x509_pb2'
  # @@protoc_insertion_point(class_scope:ostorlab.agent.message.proto.v3.fingerprint.domain_name.service.x509.Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
