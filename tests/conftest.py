import pytest

from api.client import ApiClient
from config.settings import BASE_URL, REQUEST_TIMEOUT


@pytest.fixture
def api_client():
    client = ApiClient(BASE_URL, REQUEST_TIMEOUT)
    yield client
    client.close()
