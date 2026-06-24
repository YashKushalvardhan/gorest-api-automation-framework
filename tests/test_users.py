# tests/test_users.py
import pytest
import requests
from utils.helpers import generate_random_email


def test_get_all_users(base_url, headers):
    """Get all users with pagination"""
    response = requests.get(
        f"{base_url}/users", 
        headers=headers, 
        params={"page": 1, "per_page": 20}
    )
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert isinstance(data, list)
    if len(data) > 0:
        assert "id" in data[0]
        assert "name" in data[0]


def test_create_user(base_url, headers):
    """Create a new user with random email"""
    payload = {
        "name": "Yash Test User",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    
    response = requests.post(f"{base_url}/users", json=payload, headers=headers)
    
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert "id" in data


def test_get_single_user(base_url, headers):
    """Get existing user by ID"""
    user_id = 8519404  # GoREST ka public user ID (agar fail ho to change kar dena)
    response = requests.get(f"{base_url}/users/{user_id}", headers=headers)
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert data["id"] == user_id


def test_create_user_invalid_data(base_url, headers):
    """Negative testing - missing required fields"""
    payload = {"name": "Invalid User"}  # email aur gender missing
    response = requests.post(f"{base_url}/users", json=payload, headers=headers)
    
    assert response.status_code == 422, f"Expected 422, got {response.status_code}"