from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from httpx import Response
from typing import TypedDict

class CreateUserDict(TypedDict):
    """Create new user request structure"""
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """Client for /api/v1/users endpoint"""
    def create_user_api(self, request: CreateUserDict) -> Response:
        """Create new user method:
        param request: dictionary with obligatory fields CreateUserDict
        return: Server's answer httpx.Response
        """
        return self.post("/api/v1/users", json=request)

def get_public_users_client() -> PublicUsersClient:
    """
        The function creates PublicUsersClient with all necessary preparations

        :return: ready to be used PublicUsersClient
        """
    return PublicUsersClient(client=get_public_http_client())