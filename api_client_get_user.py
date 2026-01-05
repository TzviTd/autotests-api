from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)

#post request
create_user_response = public_users_client.create_user(create_user_request)
print("Create User data:", create_user_response)

#authentication request
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

private_users_client = get_private_users_client(authentication_user)

#get request
get_user_response = private_users_client.get_user(create_user_response.user.id)
print("Get User data:", get_user_response)