# tests/test_comments.py
import pytest
import requests
from utils.logger import log_info

def test_create_comment(base_url, headers):
    log_info("Creating comment on post")
    payload = {
        "post_id": 284430,                    # Valid post ID
        "name": "Yash Tester",
        "email": "yash.test@example.com",
        "body": "Great post! Automation testing is awesome."
    }
    response = requests.post(f"{base_url}/comments", json=payload, headers=headers)
    assert response.status_code == 201