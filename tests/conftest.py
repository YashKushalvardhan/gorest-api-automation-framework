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

# Optional: Common response validator
def validate_response(response, expected_status=200):
    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"
    assert response.elapsed.total_seconds() < 3, "Response took too long"
    return response.json()