from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class CreateCourseRequestDict(TypedDict):
    """Create Course structure"""
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFieldId: str
    createdByUserId: str

class UpdateCourseRequestDict(TypedDict):
    """Update Course structure"""
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None
    previewFieldId: str | None
    createdByUserId: str | None

class GetCoursesQueryDict(TypedDict):
    """Params structure for get_course_api method"""
    userId: str

class CoursesClient(APIClient):
    """Client for /api/v1/courses"""
    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Getting full list of courses
        :param query: query params
        :return: Server's answer httpx.Response
        """
        return self.get("/api/v1/courses", params=query)

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Creating a course
        :param request: Typeddict structure
        :return: Server's answer httpx.Response
        """
        return self.post("/api/v1/courses", json=request)

    def get_course_api(self, course_id: str) -> Response:
        """
        Getting a certain course by id
        :param course_id: enter course id
        :return: Server's answer httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Updating a certain course
        :param course_id: enter course id
        :param request: Typeddict structure
        :return: Server's answer httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Deleting a course
        :param course_id: enter course id
        :return: Server's answer httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

