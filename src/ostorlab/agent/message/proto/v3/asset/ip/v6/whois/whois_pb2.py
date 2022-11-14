# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ostorlab/agent/message/proto/v3/asset/ip/v6/whois/whois.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ostorlab/agent/message/proto/v3/asset/ip/v6/whois/whois.proto',
  package='ostorlab.agent.message.proto.v3.asset.ip.v6.whois',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n=ostorlab/agent/message/proto/v3/asset/ip/v6/whois/whois.proto\x12\x31ostorlab.agent.message.proto.v3.asset.ip.v6.whois\"L\n\x07Network\x12\x0c\n\x04\x63idr\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06handle\x18\x03 \x01(\t\x12\x15\n\rparent_handle\x18\x04 \x01(\t\"E\n\x07\x43ontact\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\"c\n\x06\x45ntity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12K\n\x07\x63ontact\x18\x02 \x01(\x0b\x32:.ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Contact\"\xc2\x02\n\x07Message\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04mask\x18\x02 \x01(\t\x12\x12\n\x07version\x18\x03 \x01(\x05:\x01\x36\x12\x14\n\x0c\x61sn_registry\x18\x04 \x01(\t\x12\x12\n\nasn_number\x18\x05 \x01(\x05\x12\x18\n\x10\x61sn_country_code\x18\x06 \x01(\t\x12\x10\n\x08\x61sn_date\x18\x07 \x01(\t\x12\x17\n\x0f\x61sn_description\x18\x08 \x01(\t\x12K\n\x07network\x18\t \x01(\x0b\x32:.ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Network\x12K\n\x08\x65ntities\x18\n \x03(\x0b\x32\x39.ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Entity')
)




_NETWORK = _descriptor.Descriptor(
  name='Network',
  full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Network',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cidr', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Network.cidr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Network.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='handle', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Network.handle', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_handle', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Network.parent_handle', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=116,
  serialized_end=192,
)


_CONTACT = _descriptor.Descriptor(
  name='Contact',
  full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Contact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Contact.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Contact.kind', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Contact.address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Contact.email', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=194,
  serialized_end=263,
)


_ENTITY = _descriptor.Descriptor(
  name='Entity',
  full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Entity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Entity.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contact', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Entity.contact', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=265,
  serialized_end=364,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Message.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mask', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Message.mask', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Message.version', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=6,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asn_registry', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Message.asn_registry', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asn_number', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Message.asn_number', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asn_country_code', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Message.asn_country_code', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asn_date', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Message.asn_date', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asn_description', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Message.asn_description', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Message.network', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entities', full_name='ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Message.entities', index=9,
      number=10, type=11, cpp_type=10, label=3,
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
  serialized_start=367,
  serialized_end=689,
)

_ENTITY.fields_by_name['contact'].message_type = _CONTACT
_MESSAGE.fields_by_name['network'].message_type = _NETWORK
_MESSAGE.fields_by_name['entities'].message_type = _ENTITY
DESCRIPTOR.message_types_by_name['Network'] = _NETWORK
DESCRIPTOR.message_types_by_name['Contact'] = _CONTACT
DESCRIPTOR.message_types_by_name['Entity'] = _ENTITY
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Network = _reflection.GeneratedProtocolMessageType('Network', (_message.Message,), dict(
  DESCRIPTOR = _NETWORK,
  __module__ = 'ostorlab.agent.message.proto.v3.asset.ip.v6.whois.whois_pb2'
  # @@protoc_insertion_point(class_scope:ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Network)
  ))
_sym_db.RegisterMessage(Network)

Contact = _reflection.GeneratedProtocolMessageType('Contact', (_message.Message,), dict(
  DESCRIPTOR = _CONTACT,
  __module__ = 'ostorlab.agent.message.proto.v3.asset.ip.v6.whois.whois_pb2'
  # @@protoc_insertion_point(class_scope:ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Contact)
  ))
_sym_db.RegisterMessage(Contact)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), dict(
  DESCRIPTOR = _ENTITY,
  __module__ = 'ostorlab.agent.message.proto.v3.asset.ip.v6.whois.whois_pb2'
  # @@protoc_insertion_point(class_scope:ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Entity)
  ))
_sym_db.RegisterMessage(Entity)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'ostorlab.agent.message.proto.v3.asset.ip.v6.whois.whois_pb2'
  # @@protoc_insertion_point(class_scope:ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
