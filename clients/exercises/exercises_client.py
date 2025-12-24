from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class GetExercisesQueryDict(TypedDict):
    """Params structure for get_exercise_api method"""
    courseId: str

class CreateExerciseRequestDict(TypedDict):
    """Create Exercise structure"""
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):
    """Update Exercise structure"""
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """Client for /api/v1/exercises/"""
    def get_exercises_api(self, query:GetExercisesQueryDict) -> Response:
        """
        Getting full list of exercises
        :param query: query structure
        :return: Server's answer httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Creating a new exercise
        :param request: Typeddict structure
        :return: Server's answer httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Getting a certain exercise by id
        :param exercise_id: enter the id
        :return: Server's answer httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def update_exercise_id(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Updating an exercise
        :param exercise_id: enter the id
        :param request: Typeddict structure
        :return: Server's answer httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Deleting an exercise
        :param exercise_id: enter the id
        :return: Server's answer httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")