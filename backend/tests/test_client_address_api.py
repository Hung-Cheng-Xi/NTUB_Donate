import httpx
import pytest


@pytest.mark.asyncio
async def test_admin_get_zipcode(base_url):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{base_url}/client/address/get_zipcode/",
            json={
                "address": "臺中市西屯區臺灣大道三段99號"
            }
        )
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["zipcode"] == "40701"
        assert json_data["adrs"] == "臺中市西屯區臺灣大道三段99號"
        assert json_data["dataver6"] == "11207(beta)"
