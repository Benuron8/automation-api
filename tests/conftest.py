import pytest
import os
from dotenv import load_dotenv
from src.api_client import APIClient

# Define the base URL
BASE_URL = "https://api.themoviedb.org/3"

# Fixture to create APIClient and load environment variables
@pytest.fixture(scope="module")  # scope="module" ensures it's loaded only once per test module
def api_client():
    """Fixture to create and return an APIClient instance."""
    load_dotenv()  # Load environment variables once
    api_token = os.getenv('API_TOKEN')  # Fetch the API token from environment variables
    
    print(f"Loaded API Token: {api_token}")
    return APIClient(BASE_URL, api_token)