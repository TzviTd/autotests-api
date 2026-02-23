from clients.exercises.exercises_schema import (CreateExerciseRequestSchema, CreateExerciseResponseSchema,
                                                ExerciseSchema, GetExerciseResponseSchema,
                                                UpdateExerciseRequestSchema, UpdateExerciseResponseSchema,
                                                GetExercisesResponseSchema
                                                )
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import InternalErrorResponseSchema, assert_internal_error_response

def assert_create_exercise_response(request: CreateExerciseRequestSchema, response: CreateExerciseResponseSchema):
    """
    The function checks if request and response data coincide
    :param request: user's request
    :param response: actual response
    :raises AssertionError: if any parameter does not match
    """
    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.course_id, response.exercise.course_id, "course_id")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")

def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    The function compares the actual exercise data with the expected one
    :param actual: Actual exercise data
    :param expected: Expected data
    :raises AssertionError: if any parameter does not match
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

def assert_get_exercise_response(get_exercise_response: GetExerciseResponseSchema,
                                 create_exercise_response: CreateExerciseResponseSchema
):
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)

def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercise_responses:list[CreateExerciseResponseSchema]
):
    assert_length(get_exercises_response.exercises, create_exercise_responses, "exercises")
    for i, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(get_exercises_response.exercises[i], create_exercise_response.exercise)

def assert_update_exercise_response(request: UpdateExerciseRequestSchema, response: UpdateExerciseResponseSchema):
    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")

def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)