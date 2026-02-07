from clients.error_scheme import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_length, assert_equal

def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    The function checks if actual validation error matches the expected one
    :param actual: Actual validation error
    :param expected: Expected validation error
    :raises AssertionError: if any of parameters does not match
    """
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.location, expected.location, "location")

def assert_validation_error_response(
        actual: ValidationErrorResponseSchema,
        expected: ValidationErrorResponseSchema
):
    """
    The function checks if actual validation error response matches the scheme
    :param actual: actual API validation error response
    :param expected: expected validation error response
    :raises AssertionError: if any of parameters does not match
    """
    assert_length(actual.details, expected.details, "details")
    for i, detail in enumerate(expected.details):
        assert_validation_error(actual.details[i], detail)

def assert_create_file_with_empty_filename(actual: ValidationErrorResponseSchema):
    """
    The function checks if actual validation error response matches the scheme
    :param actual: actual API validation error response
    :raises AssertionError: if any of parameters does not match
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="", #empty input
                ctx={"min_length": 1},
                msg="String should have at least 1 character",
                location=["body", "filename"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)

def assert_create_file_with_empty_directory(actual: ValidationErrorResponseSchema):
    """
    The function checks if actual validation error response matches the scheme
    :param actual: actual API validation error response
    :raises AssertionError: if any of parameters does not match
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",  # empty input
                ctx={"min_length": 1},
                msg="String should have at least 1 character",
                loc=["body", "directory"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)

def assert_internal_error(actual: InternalErrorResponseSchema, expected: InternalErrorResponseSchema):
    """
    The function verifies the internal error. For instance, 404
    :param actual: Actual error
    :param expected: Expected error
    :raises AssertionError: if any of parameters does not match
    """
    assert_equal(actual.details, expected.details, "details")

def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    The function for checking the error when the file is not found on server
    :param actual: Actual response
    :raises AssertionError: if any of parameters does not match
    """
    expected = InternalErrorResponseSchema(details="File not found")
    assert_internal_error(actual, expected)

def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    """
    The function checks the error response when file id is incorrect
    :param actual: Actual response
    :return:
    """
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="uuid_parsing",
                input="incorrect-file-id",
                ctx={
                    "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"
                },
                msg="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                location=["path", "file_id"]
            )
        ]
    )

    assert_validation_error_response(actual, expected)