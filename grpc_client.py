import grpc

import user_service_pb2
import user_service_pb2_grpc

# Connecting to the server
channel = grpc.insecure_channel('localhost:50051')
stub = user_service_pb2_grpc.UserServiceStub(channel)

# Making a request
response = stub.GetUser(user_service_pb2.GetUserRequest(username="Tzvi"))
print(response.message)  # Выведет: Привет, {username}!
