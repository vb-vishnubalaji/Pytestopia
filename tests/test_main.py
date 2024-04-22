import pytest
import source.math as functions


def test_add():
    result = functions.add(1,2)
    assert result == 3


def test_divide():
    result = functions.divide(4,2)
    assert result == 2


@pytest.mark.skip(reason="Skipping this as there is another test function")
def test_divide_by_zero():
    with pytest.raises(ValueError):
        result = functions.divide(4,0)

def test_add_strings():
    result = functions.add("Vishnu ", "Balaji")
    assert result == "Vishnu Balaji"


@pytest.mark.xfail(reason="Anything divided by Zero is a mathematical failure")
def test_divide_by_zero_fail():
    assert functions.divide(4,0)