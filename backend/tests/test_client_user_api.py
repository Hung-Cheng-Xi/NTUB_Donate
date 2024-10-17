import httpx
import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize("user_id", [3])
async def test_client_user_get_user(base_url, user_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{base_url}/client/user/{user_id}")
        assert response.status_code == 200

        json_data = response.json()
        assert json_data["id"] == user_id
        assert json_data["account"] == "洪承熙"
