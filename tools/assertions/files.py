from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema, FileSchema
from tools.assertions.base import assert_equal
import httpx

def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    The function checks if created file matches the requested one
    :param request: User request
    :param response: API's response
    :raises AssertionError: if at least one of the parameters does not match
    """
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")

def assert_file_is_accessible(url: str):
    """
    The function checks if uploaded file actually exists and available to get it
    :param url: uploaded file's url
    :raises AssertionError: if file is not found
    """
    response = httpx.get(url)

    assert response.status_code == 200, f"Unable to get file by url: {url}"

def assert_file(actual: FileSchema, expected: FileSchema):
    """
    The function checks if uploaded file structure matches the expected one
    :param actual: API's response FileSchema
    :param expected: Expected FileSchema
    :raises AssertionError: if at least one of the parameters does not match
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")

def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    """
    Checks if get file response matches create file response
    :param get_file_response: API's get response
    :param create_file_response: API's create response
    :raises AssertionError: if at least one of the parameters does not match
    """
    assert_file(get_file_response.file, create_file_response.file)