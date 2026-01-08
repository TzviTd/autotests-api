from pydantic import BaseModel, Field, EmailStr
from tools.fakers import fake

class TokenSchema(BaseModel):
    """Token structure"""
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginRequestSchema(BaseModel):
    """Login request structure"""
    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)

class LoginResponseSchema(BaseModel):
    """Authentication response structure"""
    token: TokenSchema

class RefreshRequestSchema(BaseModel):
    """Refresh token request structure"""
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)