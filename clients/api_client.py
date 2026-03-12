from httpx import Client, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles
from typing import Any
import allure


class APIClient:
    """Basic API Client"""
    def __init__(self, client: Client):
        self.client = client

    @allure.step("Make GET request to {url}")
    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """Basic get method structure"""
        return self.client.get(url, params=params)

    @allure.step("Make POST request to {url}")
    def post(
            self, url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        """Basic post method structure"""
        return self.client.post(url, json=json, data=data, files=files)

    @allure.step("Make PATCH request to {url}")
    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """Basic patch method structure"""
        return self.client.patch(url, json=json)

    @allure.step("Make DELETE request to {url}")
    def delete(self, url: URL | str):
        """Basic delete method structure"""
        return self.client.delete(url)
