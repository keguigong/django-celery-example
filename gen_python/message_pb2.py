# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\rmessage.proto\"\xb8\x02\n\x07Message\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\t\x12\x12\n\npublish_ts\x18\x03 \x01(\x03\x12\x0b\n\x03ttl\x18\x04 \x01(\x03\x12\"\n\x04type\x18\x05 \x01(\x0e\x32\x14.Message.MessageType\x12\x10\n\x08sub_type\x18\x06 \x01(\t\x12\"\n\x06params\x18\x07 \x03(\x0b\x32\x12.Message.ParamType\x1a\'\n\tParamType\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"l\n\x0bMessageType\x12\x10\n\x0cNOTIFICATION\x10\x00\x12\x13\n\x0f\x43ONTROL_COMMAND\x10\x01\x12\x12\n\x0e\x43OMMAND_RESULT\x10\x02\x12\x0f\n\x0b\x44\x41TA_REPORT\x10\x03\x12\x11\n\rCLIENT_STATUS\x10\x04\x42.\n\x1d\x63om.nextev.messaging.protobufB\rNextEVMessage')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_MESSAGE_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='Message.MessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOTIFICATION', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_COMMAND', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_RESULT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_REPORT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_STATUS', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=222,
  serialized_end=330,
)
_sym_db.RegisterEnumDescriptor(_MESSAGE_MESSAGETYPE)


_MESSAGE_PARAMTYPE = _descriptor.Descriptor(
  name='ParamType',
  full_name='Message.ParamType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Message.ParamType.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Message.ParamType.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=220,
)

_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='Message.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Message.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='Message.publish_ts', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='Message.ttl', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Message.type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub_type', full_name='Message.sub_type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='Message.params', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MESSAGE_PARAMTYPE, ],
  enum_types=[
    _MESSAGE_MESSAGETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=330,
)

_MESSAGE_PARAMTYPE.containing_type = _MESSAGE
_MESSAGE.fields_by_name['type'].enum_type = _MESSAGE_MESSAGETYPE
_MESSAGE.fields_by_name['params'].message_type = _MESSAGE_PARAMTYPE
_MESSAGE_MESSAGETYPE.containing_type = _MESSAGE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(

  ParamType = _reflection.GeneratedProtocolMessageType('ParamType', (_message.Message,), dict(
    DESCRIPTOR = _MESSAGE_PARAMTYPE,
    __module__ = 'message_pb2'
    # @@protoc_insertion_point(class_scope:Message.ParamType)
    ))
  ,
  DESCRIPTOR = _MESSAGE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:Message)
  ))
_sym_db.RegisterMessage(Message)
_sym_db.RegisterMessage(Message.ParamType)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\035com.nextev.messaging.protobufB\rNextEVMessage'))
# @@protoc_insertion_point(module_scope)
