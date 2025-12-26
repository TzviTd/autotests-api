from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from httpx import Response
from typing import TypedDict

class Token(TypedDict):
    """Token structure"""
    tokenType: str
    accessToken: str
    refreshToken: str

class LoginRequestDict(TypedDict):
    """Login request Typedict structure"""
    email: str
    password: str

class LoginResponseDict(TypedDict):
    """Authentication response structure"""
    token: Token

class RefreshRequestDict(TypedDict):
    """Refresh token request Typedict structure"""
    refreshToken: str

class AuthenticationClient(APIClient):
    """Client for api/v1/authentication/ endpoint"""
    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Logging in method
        :param request: Typedict dictionary LoginRequestDic
        :return: Server's answer httpx.Response
        """
        return self.post("api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict):
        """
        Refreshing access token method
        :param request: Typedict dictionary RefreshRequestDict
        :return: Server's answer httpx.Response
        """
        return self.post("api/v1/authentication/refresh", json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        response = self.login_api(request) # Authentication request
        return response.json() # Getting response in json format

def get_authentication_client() -> AuthenticationClient:
    """
        The function creates AuthenticationClient with all necessary preparations

        :return: ready to be used AuthenticationClient
        """
    return AuthenticationClient(client=get_public_http_client())

