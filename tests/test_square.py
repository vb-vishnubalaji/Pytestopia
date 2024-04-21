import pytest
from source.shape import Square
import math
class TestSquare():

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.square = Square(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.square
    def test_area(self):
        assert self.square.area() == (math.pow(self.square.side,2))

    def test_perimeter(self):
        assert self.square.perimeter() == (self.square.side * 4)