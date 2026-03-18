from pydantic import BaseModel, HttpUrl, Field
from tools.fakers import fake
from pydantic import FilePath


class FileSchema(BaseModel):
    """File structure"""
    id: str
    url: HttpUrl
    filename: str
    directory: str

class CreateFileRequestSchema(BaseModel):
    """Create File TypedDict structure"""
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str = Field(default="tests")
    upload_file: FilePath

class CreateFileResponseSchema(BaseModel):
    """Create File Response structure"""
    file: FileSchema

class GetFileResponseSchema(BaseModel):
    """Get File Response structure"""
    file: FileSchema