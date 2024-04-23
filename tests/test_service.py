import pytest
import source.service as service
from unittest import mock


@mock.patch("source.service.get_data_from_db", return_value="Mocked Alice")
def test_get_data_from_db(mock_data):
    user = service.get_data_from_db(1)
    assert user == "Mocked Alice"


@mock.patch("source.service.req")
def test_get_data_from_requests():
    pass