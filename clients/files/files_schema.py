from pydantic import BaseModel, HttpUrl


class FileSchema(BaseModel):
    """File structure"""
    id: str
    url: HttpUrl
    filename: str
    directory: str

class CreateFileRequestSchema(BaseModel):
    """Create File TypedDict structure"""
    filename: str
    directory: str
    upload_file: str

class CreateFileResponseSchema(BaseModel):
    """Create File Response structure"""
    file: FileSchema