from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class CreateFileRequestDict(TypedDict):
    """Create File TypedDict structure"""
    filename: str
    directory: str
    upload_file: str

class FilesClient(APIClient):
    """Client for /api/v1/files"""
    def get_file_api(self, file_id: str) -> Response:
        """
        Getting file by id
        :param file_id: file id number
        :return: Server's answer httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Uploading a new file
        :param request: Typeddict structure
        :return: Server's answer httpx.Response
        """
        return self.post(
            "/api/v1/files",
            data=request,
            files={"upload_file": open(request["upload_file"], "rb")}
        )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Deleting a file
        :param file_id: file id number
        :return: Server's answer httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")