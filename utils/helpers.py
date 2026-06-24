# utils/helpers.py
import json
import random

def generate_random_email():
    """Unique email generate karta hai for every test run"""
    return f"testuser{random.randint(10000, 99999)}@example.com"


def load_test_data(file_name: str):
    """JSON file se test data load karne ke liye"""
    try:
        with open(f"data/{file_name}", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"data/{file_name} file nahi mila")
    except json.JSONDecodeError:
        raise ValueError(f"data/{file_name} invalid JSON hai")