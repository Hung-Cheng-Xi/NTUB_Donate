import pytest
import os


@pytest.fixture
def base_url():
    environment = os.getenv("ENVIRONMENT", "development")

    if environment == "production":
        return "http://backend:8000/api"
    elif environment == "development":
        return "http://localhost:8000/api"
    else:
        raise ValueError(f"未知的環境: {environment}")
