# tests/conftest.py
import pytest
import requests
from dotenv import load_dotenv
import os


load_dotenv()  #  to load variables from .env

BASE_URL = os.getenv("BASE_URL")
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


def validate_response(response, expected_status=200):
    assert response.status_code == expected_status, \
        f"Expected {expected_status}, got {response.status_code}. Body: {response.text[:300]}"
    assert response.elapsed.total_seconds() < 3, f"Response slow: {response.elapsed.total_seconds()}s"
    return response.json()


from utils.logger import log_info, log_error
@pytest.fixture(scope="function", autouse=True)
def log_test_start(request):
    """Logging after every start and end of test"""
    test_name = request.node.name
    log_info(f"🚀 START TEST: {test_name}")
    
    def log_test_end():
        log_info(f"🏁 END TEST: {test_name}")
    
    request.addfinalizer(log_test_end)