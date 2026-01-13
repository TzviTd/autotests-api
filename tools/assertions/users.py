from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema
from tools.assertions.base import assert_equal

def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Checking if the response data matches the request
    :param request: Outcoming create user request
    :param response: API create user response
    :raises AssertionError: if the parameters do not match
    """

    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")

def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Checking if the actual user structure matches expected one
    :param actual: User structure received from the API
    :param expected: Expected UserSchema structure
    :raises AssertionError: if the parameters do not match
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")

def assert_get_user_response(
        get_user_response: GetUserResponseSchema,
        create_user_response: CreateUserResponseSchema
):
    """
    Checking if a get user structure matches create user structure
    :param get_user_response: API response Get user
    :param create_user_response: API response Create user
    :raises AssertionError: if the parameters do not match
    """
    assert_user(get_user_response.user, create_user_response.user)