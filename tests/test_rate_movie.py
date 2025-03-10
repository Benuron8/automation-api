from src.api_client import APIClient
from tests.conftest import BASE_URL 

def test_rate_movie(api_client):
    movie_id = 2  # Replace with an actual movie ID for your tests
    rating = 8.0  # Example rating value (can be between 0.0 and 10.0)

    params = {
        'value': rating
    }

    # Scenario 1: Successful response (Status code 201)
    response = api_client.post(f"movie/{movie_id}/rating", params)
    assert response.status_code == 201
    data = response.json()
    print(data)
    assert 'status_message' in data, "Response should contain a status message"

    # Scenario 2: Unauthorized Access (Invalid API Key, Status code 401)
    invalid_client = APIClient(BASE_URL, "invalid_api_key")
    invalid_response = invalid_client.post(f"movie/{movie_id}/rating", params)
    assert invalid_response.status_code == 401

    # Scenario 3: Invalid movie ID (404 Not Found)
    invalid_movie_id = 9999999  # Invalid movie ID
    invalid_response = api_client.post(f"movie/{invalid_movie_id}/rating", params)
    assert invalid_response.status_code == 404
