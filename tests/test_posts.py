# tests/test_posts.py
import pytest
import requests
from utils.helpers import generate_random_email
from utils.logger import log_info

def test_create_post(base_url, headers):
    log_info("Creating a new post")
    payload = {
        "user_id": 8521886,           # Valid user ID
        "title": "My Automation Test Post",
        "body": "This is a test post created via pytest framework."
    }
    response = requests.post(f"{base_url}/posts", json=payload, headers=headers)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]