import requests

class APIClient:
    def __init__(self, base_url, api_token):
        self.base_url = base_url
        self.api_token = api_token

    def get(self, endpoint, params=None):
        """Sends a GET request to the API."""
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Accept': 'application/json'
        }
        response = requests.get(url, headers=headers, params=params)
        return response  # Return the entire response object, not just the JSON

    def post(self, endpoint, json=None):
        """Sends a POST request to the API."""
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Accept': 'application/json'
        }
        response = requests.post(url, headers=headers, json=json)  # Sending data in JSON format
        return response  # Return the entire response object, not just the JSON
