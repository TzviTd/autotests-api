from pydantic import BaseModel, Field, ConfigDict

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

    email: str
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """Create User Response structure"""
    user: UserSchema

class UpdateUserRequestSchema(BaseModel):
    """Update (patch) user Typedict structure"""
    model_config = ConfigDict(populate_by_name=True)

    email: str | None
    last_name: str | None = Field(alias="lastName")
    first_name: str | None = Field(alias="firstName")
    middle_name: str | None = Field(alias="middleName")

class UpdateUserResponseSchema(BaseModel):
    """Create User Response structure"""
    user: UserSchema