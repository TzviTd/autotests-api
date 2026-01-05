from pydantic import BaseModel, Field, ConfigDict

class ExerciseSchema(BaseModel):
    """Exercise structure"""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class GetExercisesQuerySchema(BaseModel):
    """Params structure for get_exercise_api method"""
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")

class GetExercisesResponseSchema(BaseModel):
    """Get Exercises list structure"""
    exercises: list[ExerciseSchema]

class GetExerciseResponseSchema(BaseModel):
    """Get one exercise structure"""
    exercise: ExerciseSchema

class UpdateExerciseResponseSchema(BaseModel):
    """Update Exercise structure"""
    exercise: ExerciseSchema

class CreateExerciseResponseSchema(BaseModel):
    """Create Exercise structure"""
    exercise: ExerciseSchema

class CreateExerciseRequestSchema(BaseModel):
    """Create Exercise structure"""
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class UpdateExerciseRequestSchema(BaseModel):
    """Update Exercise structure"""
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")