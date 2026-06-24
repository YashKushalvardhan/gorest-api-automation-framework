# tests/test_users.py
import pytest
import requests
from utils.helpers import generate_random_email, load_test_data
# tests/test_users.py top pe
from utils.logger import log_info, log_error


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
    """Create a new user"""
    log_info("Creating new user with random email")
    
    payload = {
        "name": "Yash Test User",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    
    log_info(f"Payload: {payload}")
    
    response = requests.post(f"{base_url}/users", json=payload, headers=headers)
    
    if response.status_code == 201:
        log_info("User created successfully")
    else:
        log_error(f"User creation failed. Status: {response.status_code}")
    
    assert response.status_code == 201


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



def test_update_user(base_url, headers):
    """Update existing user"""
    user_id = 8519404  # public user
    payload = {
        "name": "Yash Updated User",
        "status": "inactive"
    }
    response = requests.put(f"{base_url}/users/{user_id}", json=payload, headers=headers)
    
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["status"] == payload["status"]


def test_delete_user(base_url, headers):
    """Delete a user (create first then delete)"""
    # Step 1: Create user
    create_payload = {
        "name": "Delete Test User",
        "email": generate_random_email(),
        "gender": "female",
        "status": "active"
    }
    create_resp = requests.post(f"{base_url}/users", json=create_payload, headers=headers)
    assert create_resp.status_code == 201
    user_id = create_resp.json()["id"]
    
    # Step 2: Delete
    del_resp = requests.delete(f"{base_url}/users/{user_id}", headers=headers)
    assert del_resp.status_code == 204   # No Content


# Data Driven Testing

# ==================== Data-Driven Test ====================
test_data = load_test_data("test_users.json")["users"]   # Ab yahan import ke baad load ho raha hai

@pytest.mark.parametrize("user_data", test_data)
def test_create_multiple_users(base_url, headers, user_data):
    """Data-Driven: Multiple users create karna"""
    payload = {
        "name": user_data["name"],
        "email": generate_random_email(),
        "gender": user_data["gender"],
        "status": user_data["status"]
    }
    response = requests.post(f"{base_url}/users", json=payload, headers=headers)
    assert response.status_code == 201, f"Failed for user: {user_data['name']}"