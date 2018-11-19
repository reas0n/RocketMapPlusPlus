# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/boot_time.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.networking.platform.telemetry import platform_metric_data_pb2 as pogoprotos_dot_networking_dot_platform_dot_telemetry_dot_platform__metric__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/boot_time.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n)pogoprotos/data/telemetry/boot_time.proto\x12\x19pogoprotos.data.telemetry\x1a\x43pogoprotos/networking/platform/telemetry/platform_metric_data.proto\"\xb1\x04\n\x08\x42ootTime\x12N\n\x08\x64uration\x18\x01 \x01(\x0b\x32<.pogoprotos.networking.platform.telemetry.PlatformMetricData\x12\x41\n\nboot_phase\x18\x02 \x01(\x0e\x32-.pogoprotos.data.telemetry.BootTime.BootPhase\"\x91\x03\n\tBootPhase\x12\r\n\tUNDEFINED\x10\x00\x12\x0f\n\x0bTIME_TO_MAP\x10\x01\x12\x14\n\x10LOGO_SCREEN_TIME\x10\x02\x12\x18\n\x14MAIN_SCENE_LOAD_TIME\x10\x03\x12\x11\n\rWAIT_FOR_AUTH\x10\x04\x12\x1f\n\x1bINIT_REMOTE_CONFIG_VERSIONS\x10\x05\x12\x16\n\x12INIT_BUNDLE_DIGEST\x10\x06\x12\x0c\n\x08INIT_GMT\x10\x07\x12\x11\n\rDOWNLOAD_I18N\x10\x08\x12\x1a\n\x16\x44OWNLOAD_GLOBAL_ASSETS\x10\t\x12\x1e\n\x1aREGISTER_PUSH_NOTIFICATION\x10\n\x12\x16\n\x12INITIALIZE_UPSIGHT\x10\x0b\x12\x1a\n\x16INITIALIZE_CRITTERCISM\x10\x0c\x12\x17\n\x13LOGIN_VERSION_CHECK\x10\r\x12\x14\n\x10LOGIN_GET_PLAYER\x10\x0e\x12\x18\n\x14LOGIN_AUTHENTICATION\x10\x0f\x12\x0e\n\nMODAL_TIME\x10\x10\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_networking_dot_platform_dot_telemetry_dot_platform__metric__data__pb2.DESCRIPTOR,])



_BOOTTIME_BOOTPHASE = _descriptor.EnumDescriptor(
  name='BootPhase',
  full_name='pogoprotos.data.telemetry.BootTime.BootPhase',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIME_TO_MAP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOGO_SCREEN_TIME', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAIN_SCENE_LOAD_TIME', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAIT_FOR_AUTH', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INIT_REMOTE_CONFIG_VERSIONS', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INIT_BUNDLE_DIGEST', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INIT_GMT', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOAD_I18N', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOAD_GLOBAL_ASSETS', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_PUSH_NOTIFICATION', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INITIALIZE_UPSIGHT', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INITIALIZE_CRITTERCISM', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOGIN_VERSION_CHECK', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOGIN_GET_PLAYER', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOGIN_AUTHENTICATION', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODAL_TIME', index=16, number=16,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=302,
  serialized_end=703,
)
_sym_db.RegisterEnumDescriptor(_BOOTTIME_BOOTPHASE)


_BOOTTIME = _descriptor.Descriptor(
  name='BootTime',
  full_name='pogoprotos.data.telemetry.BootTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='duration', full_name='pogoprotos.data.telemetry.BootTime.duration', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boot_phase', full_name='pogoprotos.data.telemetry.BootTime.boot_phase', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BOOTTIME_BOOTPHASE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=703,
)

_BOOTTIME.fields_by_name['duration'].message_type = pogoprotos_dot_networking_dot_platform_dot_telemetry_dot_platform__metric__data__pb2._PLATFORMMETRICDATA
_BOOTTIME.fields_by_name['boot_phase'].enum_type = _BOOTTIME_BOOTPHASE
_BOOTTIME_BOOTPHASE.containing_type = _BOOTTIME
DESCRIPTOR.message_types_by_name['BootTime'] = _BOOTTIME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BootTime = _reflection.GeneratedProtocolMessageType('BootTime', (_message.Message,), dict(
  DESCRIPTOR = _BOOTTIME,
  __module__ = 'pogoprotos.data.telemetry.boot_time_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.BootTime)
  ))
_sym_db.RegisterMessage(BootTime)


# @@protoc_insertion_point(module_scope)
