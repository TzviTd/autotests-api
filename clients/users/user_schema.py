from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake

class UserSchema(BaseModel):
    """User structure"""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """Create new user request structure"""
    model_config = ConfigDict(populate_by_name=True)

    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)

class CreateUserResponseSchema(BaseModel):
    """Create User Response structure"""
    user: UserSchema

class UpdateUserRequestSchema(BaseModel):
    """Update (patch) user Typedict structure"""
    model_config = ConfigDict(populate_by_name=True)

    email: str | None = Field(default_factory=fake.email)
    last_name: str | None = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str | None = Field(alias="middleName", default_factory=fake.middle_name)

class UpdateUserResponseSchema(BaseModel):
    """Create User Response structure"""
    user: UserSchema

class GetUserResponseSchema(BaseModel):
    """Get User Response structure"""
    user: UserSchema