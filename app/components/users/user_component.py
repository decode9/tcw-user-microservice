import grpc

import user_pb2 as user_proto

class UserStub(object):

    def __init__(self, channel):
        pass
        self.SaveData = channel.unary_unary(
            '/Data/SaveData',
            request_serializer=user_proto.Data.SerializeToString,
            response_deserializer=user_proto.DataResponse.FromString,
        )
        self.GetData = channel.unary_unary(
            '/Data/GetData',
            request_serializer=user_proto.Empty.SerializeToString,
            response_deserializer=user_proto.DataMultipleResponse.FromString,
        )

class UserService(object):
    
    def SaveData(self,request,context):

        