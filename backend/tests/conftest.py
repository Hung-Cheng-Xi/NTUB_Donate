import pytest


def pytest_generate_tests(metafunc):
    if "environment" in metafunc.fixturenames:
        metafunc.parametrize(
            "environment", ["development", "production"])


@pytest.fixture
def base_url(environment):
    if environment == "production":
        return "http://120.97.28.11:8081/api"
    elif environment == "development":
        return "http://localhost:8000/api"
    else:
        raise ValueError(f"未知的環境: {environment}")
