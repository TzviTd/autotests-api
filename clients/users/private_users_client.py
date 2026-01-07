from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.users.user_schema import UpdateUserRequestSchema, UpdateUserResponseSchema, GetUserResponseSchema


class PrivateUsersClient(APIClient):
    """Client for private methods for /api/v1/users/ endpoint"""
    def get_user_me_api(self) -> Response:
        """
        Getting current user method
        :return: Server's answer httpx.Response
        """
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Getting certain user by user_id method
        :param user_id: introduce id (string)
        :return: Server's answer httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Updating user method
        :param user_id: introduce id (string)
        :param request: Typedict dictionary UpdateUserRequestDict
        :return: Server's answer httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True))

    def delete_user_api(self, user_id: str) -> Response:
        """
        Deleting user method
        :param user_id: introduce id (string)
        :return: Server's answer httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
        The function creates PrivateUsersClient with all necessary preparations

        :return: ready to be used PrivateUsersClient
        """
    return PrivateUsersClient(client=get_private_http_client(user))