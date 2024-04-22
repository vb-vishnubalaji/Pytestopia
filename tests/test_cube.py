import pytest
import math
from source.shape import Cube


@pytest.mark.cube_area
def test_area(cube_object):
    assert cube_object.area() == 6 * math.pow(cube_object.side, 2)


@pytest.mark.cube_perimeter
def test_perimeter(cube_object):
    assert cube_object.perimeter() == 12 * cube_object.side


@pytest.mark.cube_obj_compare
def test_cube_objects_compare(cube_object, cube_object_other):
    assert cube_object != cube_object_other


@pytest.mark.cube_area_compare
def test_cube_area_compare(cube_object, cube_object_other):
    assert cube_object.area() != cube_object_other.area()