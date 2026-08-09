# utils/helpers.py
import json
import random

def generate_random_email():
    """Generate Unique email for every test run"""
    return f"testuser{random.randint(10000, 99999)}@example.com"


def load_test_data(file_name: str):
    """ To Load test data from JSON file"""
    try:
        with open(f"data/{file_name}", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"data/{file_name} file not found")
    except json.JSONDecodeError:
        raise ValueError(f"data/{file_name} invalid JSON")