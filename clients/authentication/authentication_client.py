from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from httpx import Response
from typing import TypedDict
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema, RefreshRequestSchema

class AuthenticationClient(APIClient):
    """Client for api/v1/authentication/ endpoint"""
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Logging in method
        :param request: Typedict dictionary LoginRequestDic
        :return: Server's answer httpx.Response
        """
        return self.post("api/v1/authentication/login", json=request.model_dump(by_alias=True))

    def refresh_api(self, request: RefreshRequestSchema):
        """
        Refreshing access token method
        :param request: Typedict dictionary RefreshRequestDict
        :return: Server's answer httpx.Response
        """
        return self.post("api/v1/authentication/refresh", json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request) # Authentication request
        return LoginResponseSchema.model_validate_json(response.text) #validation json schema
        #return LoginResponseSchema(**response.json())

def get_authentication_client() -> AuthenticationClient:
    """
        The function creates AuthenticationClient with all necessary preparations

        :return: ready to be used AuthenticationClient
        """
    return AuthenticationClient(client=get_public_http_client())

