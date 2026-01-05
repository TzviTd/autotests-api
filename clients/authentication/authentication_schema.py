from pydantic import BaseModel, Field, EmailStr

class TokenSchema(BaseModel):
    """Token structure"""
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginRequestSchema(BaseModel):
    """Login request structure"""
    email: EmailStr
    password: str

class LoginResponseSchema(BaseModel):
    """Authentication response structure"""
    token: TokenSchema

class RefreshRequestSchema(BaseModel):
    """Refresh token request structure"""
    refresh_token: str = Field(alias="refreshToken")