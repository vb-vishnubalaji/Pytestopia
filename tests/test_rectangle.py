from source.shape import Rectangle
import pytest


class TestRectangle:

    @pytest.mark.parametrize("length, breadth, expected_area", [(5, 10, 50), (10, 10, 100), (2, 2, 4), (50, 2, 100)])
    def test_multiple_rectangle_areas(self, length, breadth, expected_area):
        assert Rectangle(length, breadth).area() == expected_area
