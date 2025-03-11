import requests

BASE_URL = "https://api.themoviedb.org/3"

def api_get(endpoint, params=None, api_token=None):
    url = f"{BASE_URL}/{endpoint}"
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers, params=params)
    return response

def api_post(endpoint, json=None, api_token=None):
    url = f"{BASE_URL}/{endpoint}"
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Accept': 'application/json'
    }
    response = requests.post(url, headers=headers, json=json)
    return response
