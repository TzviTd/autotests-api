import uuid
from pydantic import BaseModel, ConfigDict, Field, EmailStr
from pydantic.alias_generators import to_camel



class UserSchema(BaseModel):
    """User structure description"""
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: str
    last_name: str
    first_name: str
    middle_name: str

class CreateUserRequestSchema(BaseModel):
    """Creating User request structure description"""
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    email: EmailStr
    password: str
    last_name: str
    first_name: str
    middle_name: str

class CreateUserResponseSchema(BaseModel):
    """Creating User response description"""
    user: UserSchema
