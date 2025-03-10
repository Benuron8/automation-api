from src.api_client import APIClient
from tests.conftest import BASE_URL  # Make sure you import APIClient correctly

def test_top_rated_movies(api_client):
    params = {
        'language': 'en-US',
        'page': 1
    }

    # Send the request using the APIClient
    response = api_client.get("movie/top_rated", params)

    # Scenario 1: Successful response (Status code 200)
    assert response.status_code == 200
    data = response.json()  # Call .json() to get the response body as a dictionary
    assert isinstance(data, dict), "Response should be a dictionary"
    assert isinstance(data['results'], list), "Results should be a list"
    assert len(data['results']) > 0, "There should be at least one movie"
    assert 'title' in data['results'][0], "The first movie should have a 'title' field"
    assert 'vote_average' in data['results'][0], "The first movie should have a 'vote_average' field"

    # Scenario 2: Unauthorized (Invalid API Key, Status code 401)
    invalid_client = APIClient(BASE_URL, "invalid_api_key")
    invalid_response = invalid_client.get("movie/top_rated", params)
    assert invalid_response.status_code == 401

    # Scenario 3: Invalid endpoint (Status code 404)
    invalid_response = api_client.get("invalid/endpoint", params)
    assert invalid_response.status_code == 404