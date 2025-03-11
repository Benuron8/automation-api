import pytest
from src.api_utils import *
from src.utils import *
from tests.conftest import API_TOKEN

# Parameterized test for successful rating scenario (status code: 201)
@pytest.mark.parametrize("movie_id, rating", [
    (2, 8.0),
    (10, 7.5), 
    (15, 9.0),
])
def test_rate_movie_valid(movie_id, rating):
    params = {'value': rating}

    response = api_post(f"movie/{movie_id}/rating", params, API_TOKEN)
    assert response.status_code == 201
    
    data = response.json()

    expected_success = True
    expected_success_message = "The item/record was updated successfully."

    assert data["success"] == expected_success, f"Expected {expected_success}, got {data['success']}"
    assert data["status_message"] == expected_success_message, f"Expected {expected_success_message}, got {data['status_message']}"

# Test for invalid API key (status code: 401)
def test_rate_movie_invalid_api_key():
    movie_id = 2
    rating = 8.0

    params = {'value': rating}

    invalid_response = api_post(f"movie/{movie_id}/rating", params, "invalid_api_key")
    assert invalid_response.status_code == 401

# Test for non-existing movie ID (status code: 404 Not Found))
def test_rate_movie_non_existing_movie():
    invalid_movie_id = 9999999  # Invalid movie ID
    rating = 8.0

    params = {'value': rating}

    invalid_response = api_post(f"movie/{invalid_movie_id}/rating", params, API_TOKEN)
    assert invalid_response.status_code == 404
