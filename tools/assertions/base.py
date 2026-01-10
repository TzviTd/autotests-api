from typing import Any

def assert_status_code(actual: int, expected: int):
    """
    The function checks if the actual status code of the response matches the expected one
    :param actual: Response status code
    :param expected: Expected status code
    :raises AssertionError: if the parameters do not match
    """
    assert actual == expected, (
        f'Incorrect status code. '
        f'Expected status code: {expected}. '
        f'Actual status code: {actual}'
    )

def assert_equal(actual: Any, expected: Any, name: str):
    """
    This general function checks if actual value matches the expected one
    :param actual: Response value
    :param expected: Expected value
    :param name: This value name
    :raises Assertion Error: if the parameters do not match
    """
    assert actual == expected, (
        f'Incorrect value:"{name}". '
        f'Expected value: "{expected}". '
        f'Actual value: "{actual}"'
    )

def assert_is_true(actual: Any, name: str):
    """
    This general function checks if actual value is true
    :param actual: Response value
    :param name: This value name
    :raises AssertionError: if actual value is false
    """
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true, but got "{actual}"'
    )