# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: oss/northbound/device2cloud/common/LocalConfiguration.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='oss/northbound/device2cloud/common/LocalConfiguration.proto',
  package='oss.northbound',
  syntax='proto2',
  serialized_pb=_b('\n;oss/northbound/device2cloud/common/LocalConfiguration.proto\x12\x0eoss.northbound\"X\n\x12LocalConfiguration\x12\x42\n\x12\x63onfiguration_info\x18\x02 \x03(\x0b\x32&.oss.northbound.LocalConfigurationInfo\"\xe1\x01\n\x16LocalConfigurationInfo\x12\x19\n\x11\x63onfiguration_key\x18\x01 \x01(\t\x12\x1b\n\x13\x63onfiguration_value\x18\x02 \x01(\x0c\x12^\n$local_configuration_info_access_type\x18\x03 \x01(\x0e\x32\x30.oss.northbound.LocalConfigurationInfoAccessType\x12\x18\n\x10has_been_updated\x18\x04 \x01(\x08\x12\x15\n\rfailureReason\x18\x05 \x01(\t*K\n LocalConfigurationInfoAccessType\x12\x12\n\x0eLCIAT_READONLY\x10\x00\x12\x13\n\x0fLCIAT_READWRITE\x10\x01\x42[\n@com.nextev.pm.oss.common.protobuf.northbound.device2cloud.commonB\x17LocalConfigurationProto')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_LOCALCONFIGURATIONINFOACCESSTYPE = _descriptor.EnumDescriptor(
  name='LocalConfigurationInfoAccessType',
  full_name='oss.northbound.LocalConfigurationInfoAccessType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LCIAT_READONLY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LCIAT_READWRITE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=397,
  serialized_end=472,
)
_sym_db.RegisterEnumDescriptor(_LOCALCONFIGURATIONINFOACCESSTYPE)

LocalConfigurationInfoAccessType = enum_type_wrapper.EnumTypeWrapper(_LOCALCONFIGURATIONINFOACCESSTYPE)
LCIAT_READONLY = 0
LCIAT_READWRITE = 1



_LOCALCONFIGURATION = _descriptor.Descriptor(
  name='LocalConfiguration',
  full_name='oss.northbound.LocalConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='configuration_info', full_name='oss.northbound.LocalConfiguration.configuration_info', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=79,
  serialized_end=167,
)


_LOCALCONFIGURATIONINFO = _descriptor.Descriptor(
  name='LocalConfigurationInfo',
  full_name='oss.northbound.LocalConfigurationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='configuration_key', full_name='oss.northbound.LocalConfigurationInfo.configuration_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='configuration_value', full_name='oss.northbound.LocalConfigurationInfo.configuration_value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local_configuration_info_access_type', full_name='oss.northbound.LocalConfigurationInfo.local_configuration_info_access_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_been_updated', full_name='oss.northbound.LocalConfigurationInfo.has_been_updated', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='failureReason', full_name='oss.northbound.LocalConfigurationInfo.failureReason', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=170,
  serialized_end=395,
)

_LOCALCONFIGURATION.fields_by_name['configuration_info'].message_type = _LOCALCONFIGURATIONINFO
_LOCALCONFIGURATIONINFO.fields_by_name['local_configuration_info_access_type'].enum_type = _LOCALCONFIGURATIONINFOACCESSTYPE
DESCRIPTOR.message_types_by_name['LocalConfiguration'] = _LOCALCONFIGURATION
DESCRIPTOR.message_types_by_name['LocalConfigurationInfo'] = _LOCALCONFIGURATIONINFO
DESCRIPTOR.enum_types_by_name['LocalConfigurationInfoAccessType'] = _LOCALCONFIGURATIONINFOACCESSTYPE

LocalConfiguration = _reflection.GeneratedProtocolMessageType('LocalConfiguration', (_message.Message,), dict(
  DESCRIPTOR = _LOCALCONFIGURATION,
  __module__ = 'oss.northbound.device2cloud.common.LocalConfiguration_pb2'
  # @@protoc_insertion_point(class_scope:oss.northbound.LocalConfiguration)
  ))
_sym_db.RegisterMessage(LocalConfiguration)

LocalConfigurationInfo = _reflection.GeneratedProtocolMessageType('LocalConfigurationInfo', (_message.Message,), dict(
  DESCRIPTOR = _LOCALCONFIGURATIONINFO,
  __module__ = 'oss.northbound.device2cloud.common.LocalConfiguration_pb2'
  # @@protoc_insertion_point(class_scope:oss.northbound.LocalConfigurationInfo)
  ))
_sym_db.RegisterMessage(LocalConfigurationInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n@com.nextev.pm.oss.common.protobuf.northbound.device2cloud.commonB\027LocalConfigurationProto'))
# @@protoc_insertion_point(module_scope)