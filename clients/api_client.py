from httpx import Client, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles
from typing import Any


class APIClient:
    """Basic API Client"""
    def __init__(self, client: Client):
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """Basic get method structure"""
        return self.client.get(url, params=params)

    def post(
            self, url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        """Basic post method structure"""
        return self.client.post(url, json=json, data=data, files=files)

    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """Basic patch method structure"""
        return self.patch(url, json=json)

    def delete(self, url: URL | str):
        """Basic delete method structure"""
        return self.delete(url)
