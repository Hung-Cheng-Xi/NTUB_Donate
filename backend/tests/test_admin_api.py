import httpx
import pytest


@pytest.mark.asyncio
async def test_get_admin_test(base_url):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{base_url}/admin/test/test")
        assert response.status_code == 200
        json_data = response.json()
        assert json_data == "test"
