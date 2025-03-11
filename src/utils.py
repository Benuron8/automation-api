def verify_response_structure(data):
    assert 'results' in data, "Response should contain a 'results' field"
    assert len(data['results']) > 0, "There should be returned at least one movie"
    
    # fields for each movie
    assert 'title' in data['results'][0], "The first movie should have a 'title' field"
    assert 'vote_average' in data['results'][0], "The first movie should have a 'vote_average' field"
    assert 'vote_count' in data['results'][0], "The first movie should have a 'vote_count' field"

def verify_error_response(data, expected_status_code, expected_status_message, expected_success):
    assert data["status_code"] == expected_status_code, f"Status code expected {expected_status_code}, got {data["status_code"]}"
    assert data["status_message"] == expected_status_message, f"Status message expected {expected_status_message}, got {data["status_message"]}"
    assert data["success"] == expected_success, f"Success expected {expected_success}, got {data["success"]}"
