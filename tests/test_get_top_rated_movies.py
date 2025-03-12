from src.api_utils import *
from src.utils import *
from tests.conftest import API_TOKEN

params = {
    'language': 'en-US',
    'page': 1
}

def test_top_rated_movies_valid_api_key():
    # Gets the response the GET request
    response = api_get("movie/top_rated", params, API_TOKEN)

    # validating response status code 
    assert response.status_code == 200

    data = response.json()
    # verifying the response structure
    verify_response_structure(data)

    # verifying total movies being returned
    assert data["total_results"] > 0
    
# Test for invalid API key (status code: 401)
def test_top_rated_movies_invalid_api_key():
    invalid_response = api_get("movie/top_rated", params, "invalid_api_key")

    # validating response status code 
    assert invalid_response.status_code == 401

    # expected values
    expected_status_code = 7
    expected_status_message = "Invalid API key: You must be granted a valid key."
    expected_success = False

    data = invalid_response.json()
    verify_error_response(data, expected_status_code, expected_status_message, expected_success)

    assert data["status_code"] == expected_status_code, f"Status code expected {expected_status_code}, got {data['status_code']}"
    assert data["status_message"] == expected_status_message, f"Status message expected {expected_status_message}, got {data['status_message']}"
    assert data["success"] == expected_success, f"Success expected {expected_success}, got {data['success']}"

# Test for invalid endpoint (status code: 404 Not Found))
def test_top_rated_movies_invalid_endpoint():
    invalid_response = api_get("invalid/endpoint", params, API_TOKEN)

    # validating response status code 
    assert invalid_response.status_code == 404

    # expected values
    expected_status_code = 34
    expected_status_message = "The resource you requested could not be found."
    expected_success = False

    data = invalid_response.json()
    verify_error_response(data, expected_status_code, expected_status_message, expected_success)

    