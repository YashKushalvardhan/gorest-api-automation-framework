# tests/conftest.py
import pytest
import requests
from dotenv import load_dotenv
import os


load_dotenv()  #  to load variables from .env

BASE_URL = "https://gorest.co.in/public/v2"
TOKEN = os.getenv("GO_REST_TOKEN")  

@pytest.fixture(scope="session")
def headers():
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

# # Optional: Common response validator
# def validate_response(response, expected_status=200):
#     assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"
#     assert response.elapsed.total_seconds() < 3, "Response took too long"
#     return response.json()

def validate_response(response, expected_status=200):
    assert response.status_code == expected_status, \
        f"Expected {expected_status}, got {response.status_code}. Body: {response.text[:300]}"
    assert response.elapsed.total_seconds() < 3, f"Response slow: {response.elapsed.total_seconds()}s"
    return response.json()



# tests/conftest.py ke end mein add karo
from utils.logger import log_info, log_error
@pytest.fixture(scope="function", autouse=True)
def log_test_start(request):
    """Har test ke start aur end mein log karega"""
    test_name = request.node.name
    log_info(f"🚀 START TEST: {test_name}")
    
    def log_test_end():
        log_info(f"🏁 END TEST: {test_name}")
    
    request.addfinalizer(log_test_end)