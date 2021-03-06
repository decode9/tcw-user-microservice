from .user_pb2_grpc import DataProcessorServicer, add_DataProcessorServicer_to_server
from ...utils import Database, BusService
from . import user_pb2 as user_proto


class UserController(DataProcessorServicer):

    def __init__(self):
        self.db = Database()
        self.bus = BusService(None)

    def GetData(self, request, context):
        try:
            print("Enter Get Method")

            metadata = context.invocation_metadata()

            print('Verify Auth')

            auth = self.verify_authentication(metadata)

            if not auth['result']:
                raise Exception(auth['message'])

            users = self.db.find('users')
            
            data = []

            if users['count']:
                data = users['data']

            print('Get Response')
            response = user_proto.DataMultipleResponse(
                data=list(data)
            )
            print('Return Response')

            return response
        except Exception as error:
            print(error)
            context.set_code(500)
            context.set_details(str(error))
            raise AssertionError(str(error))

    def PostData(self, request, context):

        try:
            data = {
                "name": request.name,
                "lastname": request.lastname,
                "identification": request.identification,
                "type_identification": request.type_identification,
                "phone_number": request.phone_number
            }

            data = self.db.insert_one('users', data)

            response = user_proto.DataResponse(data=data)

            return response
        except Exception as error:
            print(error)
            context.set_code(500)
            context.set_details('Explode')
            raise AssertionError('Explode')

    def PutData(self, request, context):

        try:
            data = {
                "name": request.name,
                "lastname": request.lastname,
                "identification": request.identification,
                "type_identification": request.type_identification,
                "phone_number": request.phone_number
            }

            print('UPDATE')
            print(request._id)

            data = self.db.update_one('users', {"_id": request._id}, data)

            response = user_proto.DataResponse(data=data)

            return response
        except Exception as error:
            print(error)
            context.set_code(500)
            context.set_details('Explode')
            raise AssertionError('Explode')

    def DeleteData(self, request, context):

        try:
            data = {
                "_id": request._id,
            }

            data = self.db.delete_one('users', data)

            response = user_proto.DataResponse(data=data)

            return response
        except Exception as error:
            print(error)
            context.set_code(500)
            context.set_details('Explode')
            raise AssertionError('Explode')

    def verify_authentication(self, metadata):

        access_token = ''

        for meta in metadata:
            if meta.key == 'access_token':
                access_token = meta.value

        params = {
            'access_token': access_token
        }

        self.bus.TransmitChannel()

        print('BUS CALL')
        print(params)

        response = self.bus.call('rpc_queue',params)

        print(response)

        return response

    def add_service_to_server(self, service, server):
        add_DataProcessorServicer_to_server(service, server)
