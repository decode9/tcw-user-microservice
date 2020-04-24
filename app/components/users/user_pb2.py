# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='user.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\nuser.proto\"\x07\n\x05\x45mpty\"g\n\x04\x44\x61ta\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08lastname\x18\x03 \x01(\t\x12\x16\n\x0eidentification\x18\x04 \x01(\t\x12\x1b\n\x13type_identification\x18\x05 \x01(\x05\"#\n\x0c\x44\x61taResponse\x12\x13\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x05.Data\"+\n\x14\x44\x61taMultipleResponse\x12\x13\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x05.Data2\xa4\x01\n\rDataProcessor\x12\"\n\x08SaveData\x12\x05.Data\x1a\r.DataResponse\"\x00\x12*\n\x07GetData\x12\x06.Empty\x1a\x15.DataMultipleResponse\"\x00\x12$\n\nUpdateData\x12\x05.Data\x1a\r.DataResponse\"\x00\x12\x1d\n\nDeleteData\x12\x05.Data\x1a\x06.Empty\"\x00\x62\x06proto3'
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
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
  serialized_start=14,
  serialized_end=21,
)


_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Data.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Data.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastname', full_name='Data.lastname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identification', full_name='Data.identification', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_identification', full_name='Data.type_identification', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=126,
)


_DATARESPONSE = _descriptor.Descriptor(
  name='DataResponse',
  full_name='DataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='DataResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=163,
)


_DATAMULTIPLERESPONSE = _descriptor.Descriptor(
  name='DataMultipleResponse',
  full_name='DataMultipleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='DataMultipleResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=208,
)

_DATARESPONSE.fields_by_name['data'].message_type = _DATA
_DATAMULTIPLERESPONSE.fields_by_name['data'].message_type = _DATA
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['DataResponse'] = _DATARESPONSE
DESCRIPTOR.message_types_by_name['DataMultipleResponse'] = _DATAMULTIPLERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
  'DESCRIPTOR' : _DATA,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:Data)
  })
_sym_db.RegisterMessage(Data)

DataResponse = _reflection.GeneratedProtocolMessageType('DataResponse', (_message.Message,), {
  'DESCRIPTOR' : _DATARESPONSE,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:DataResponse)
  })
_sym_db.RegisterMessage(DataResponse)

DataMultipleResponse = _reflection.GeneratedProtocolMessageType('DataMultipleResponse', (_message.Message,), {
  'DESCRIPTOR' : _DATAMULTIPLERESPONSE,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:DataMultipleResponse)
  })
_sym_db.RegisterMessage(DataMultipleResponse)



_DATAPROCESSOR = _descriptor.ServiceDescriptor(
  name='DataProcessor',
  full_name='DataProcessor',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=211,
  serialized_end=375,
  methods=[
  _descriptor.MethodDescriptor(
    name='SaveData',
    full_name='DataProcessor.SaveData',
    index=0,
    containing_service=None,
    input_type=_DATA,
    output_type=_DATARESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetData',
    full_name='DataProcessor.GetData',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_DATAMULTIPLERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateData',
    full_name='DataProcessor.UpdateData',
    index=2,
    containing_service=None,
    input_type=_DATA,
    output_type=_DATARESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteData',
    full_name='DataProcessor.DeleteData',
    index=3,
    containing_service=None,
    input_type=_DATA,
    output_type=_EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATAPROCESSOR)

DESCRIPTOR.services_by_name['DataProcessor'] = _DATAPROCESSOR

# @@protoc_insertion_point(module_scope)