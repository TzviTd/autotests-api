from clients.api_client import APIClient
from httpx import Response
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema, UpdateCourseRequestSchema, GetCoursesQuerySchema


class CoursesClient(APIClient):
    """Client for /api/v1/courses"""
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Getting full list of courses
        :param query: query params
        :return: Server's answer httpx.Response
        """
        return self.get("/api/v1/courses", params=query.model_dump(by_alias=True))

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Creating a course
        :param request: Typeddict structure
        :return: Server's answer httpx.Response
        """
        return self.post("/api/v1/courses", json=request.model_dump(by_alias=True))

    def get_course_api(self, course_id: str) -> Response:
        """
        Getting a certain course by id
        :param course_id: enter course id
        :return: Server's answer httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Updating a certain course
        :param course_id: enter course id
        :param request: Typeddict structure
        :return: Server's answer httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request.model_dump(by_alias=True))

    def delete_course_api(self, course_id: str) -> Response:
        """
        Deleting a course
        :param course_id: enter course id
        :return: Server's answer httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    The function creates CoursesClient with all necessary preparations

    :return: ready to be used CoursesClient
    """
    return CoursesClient(client=get_private_http_client(user))

