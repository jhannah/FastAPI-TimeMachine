from fastapi.testclient import TestClient
from main import app
import time_machine
import datetime as dt
import pytest

client = TestClient(app)


@pytest.mark.asyncio
async def test_time_machine_in_the_deep_past():
	assert dt.datetime.now() != dt.datetime(2012, 1, 14)
	with time_machine.travel("2012-01-14"):
		assert dt.datetime.now() == dt.datetime(2012, 1, 14)
	assert dt.datetime.now() != dt.datetime(2012, 1, 14)


def test_time_machine_in_the_deep_past_with_app():
	assert dt.datetime.now() != dt.datetime(2012, 1, 14)
	with time_machine.travel("2012-01-14"):
		assert dt.datetime.now() == dt.datetime(2012, 1, 14)
		res = client.get("/")
		print(res.json())
		assert res.status_code == 200
		res_json = res.json()
		api_date = dt.datetime.strptime(res_json["now"], '%Y-%m-%d %H:%M:%S.%f')
		assert api_date.date() == dt.datetime(2012, 1, 14).date()
	assert dt.datetime.now() != dt.datetime(2012, 1, 14)
	res = client.get("/")
	print(res.json())
	assert res.status_code == 200
	res_json = res.json()
	api_date = dt.datetime.strptime(res_json["now"], '%Y-%m-%d %H:%M:%S.%f')
	assert api_date.date() == dt.datetime.now().date()
