from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class UpdateUserRequestDict(TypedDict):
    """Update (patch) user Typedict structure"""
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

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

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Updating user method
        :param user_id: introduce id (string)
        :param request: Typedict dictionary UpdateUserRequestDict
        :return: Server's answer httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Deleting user method
        :param user_id: introduce id (string)
        :return: Server's answer httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")