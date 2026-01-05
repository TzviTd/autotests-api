import uuid
from pydantic import BaseModel, ConfigDict, Field, EmailStr
from pydantic.alias_generators import to_camel


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    max_score: int
    min_score: int
    description: str
    estimated_time: str

course_default_model = CourseSchema(
    id="course_id",
    title="Eloquency",
    max_score=100,
    min_score=0,
    description="course",
    estimated_time="228 hours"
)

print("Course default model:", course_default_model)

course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}
course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)