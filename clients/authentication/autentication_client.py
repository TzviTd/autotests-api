from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class LoginRequestDict(TypedDict):
    """Login request Typedict structure"""
    email: str
    password: str

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


