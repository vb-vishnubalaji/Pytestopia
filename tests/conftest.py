import pytest
from source.shape import Cube


@pytest.fixture
def cube_object():
    return Cube(10)


@pytest.fixture
def cube_object_other():
    return Cube(20)