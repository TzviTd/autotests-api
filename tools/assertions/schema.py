from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator

def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    The function checks if a json-Object is matching a corresponding scheme
    :param instance: json received
    :param schema: expected schema
    :raises jsonschema.exceptions.ValidationError: If instance is not matching schema
    """
    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )