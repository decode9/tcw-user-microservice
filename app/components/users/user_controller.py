from .user_grpc import UserService
from . import user_pb2 as user_proto


class UserController(UserService):

    def GetData(self, request, context):
        response = user_proto.DataMultipleResponse(
            data=[
                {
                    "id": 1,
                    "name": 'Jorge',
                    "lastname": "Bastidas",
                    "identification": "24181317",
                    "type_identification": 2
                },
                {
                    "id": 2,
                    "name": 'Luis',
                    "lastname": "Perez",
                    "identification": "18568986",
                    "type_identification": 2
                }
            ]
        )

        return response

    def SaveData(self, request, context):
        response = user_proto.DataResponse(
            data={
                "id": request.id,
                "name": request.name,
                "lastname": request.lastname,
                "identification": request.identification,
                "type_identification": request.type_identification
            }
        )

        return response
