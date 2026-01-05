from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from tools.fakers import get_random_email

#creating user
public_users_client = get_public_users_client()
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

create_user_response = public_users_client.create_user(create_user_request)
print("Create User data:", create_user_response)

#authentication
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

#creating specialized clients
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)

create_file_response = files_client.create_file(create_file_request)
print("Create File response:", create_file_response)


create_course_request = CreateCourseRequestSchema(
title="Course 1",
    maxScore=100,
    minScore=0,
    description="descr Course 1",
    estimatedTime="2 ms",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)

create_course_response = courses_client.create_course(create_course_request)
print("Create Course response:", create_course_response)

create_exercise_request = CreateExerciseRequestSchema(
    title="Exercise 1",
    courseId=create_course_response.course.id,
    maxScore=10,
    minScore=0,
    orderIndex=0,
    description="descr Exercise 1",
    estimatedTime="5 min"
)

create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print("Create Exercise response:", create_exercise_response)

