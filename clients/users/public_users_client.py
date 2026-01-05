from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from httpx import Response
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(APIClient):
    """Client for /api/v1/users endpoint"""
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """Create new user method:
        param request: dictionary with obligatory fields CreateUserDict
        return: Server's answer httpx.Response
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)

def get_public_users_client() -> PublicUsersClient:
    """
        The function creates PublicUsersClient with all necessary preparations

        :return: ready to be used PublicUsersClient
        """
    return PublicUsersClient(client=get_public_http_client())