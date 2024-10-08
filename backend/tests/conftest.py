import pytest
import os


@pytest.fixture
def base_url():
    environment = os.getenv("ENVIRONMENT", "development")

    if environment == "production":
        return "http://120.97.28.11:8081/api"
    elif environment == "development":
        return "http://localhost:8000/api"
    else:
        raise ValueError(f"未知的環境: {environment}")
