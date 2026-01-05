from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.user_schema import UserSchema

class CourseSchema(BaseModel):
    """Course structure"""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")

class CreateCourseRequestSchema(BaseModel):
    """Create Course structure"""
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")

class CreateCourseResponseSchema(BaseModel):
    """Create course response structure"""
    course: CourseSchema

class UpdateCourseRequestSchema(BaseModel):
    """Update Course structure"""
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")

class GetCoursesQuerySchema(BaseModel):
    """Params structure for get_course_api method"""
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")