import pytest

from src.customexceptions import NotValidFigure
from src.figure import Figure
from src.square import Square

@pytest.fixture
def valid_square():
    return Square(10)


def test_valid_square(valid_square):
    assert valid_square is not None


def test_negative_side():
    with pytest.raises(NotValidFigure):
        Square(-10)


def test_not_parse_to_float_side():
    with pytest.raises(ValueError):
        Square("Ghbdfa")


def test_parse_to_float_radius():
    assert Square("3.14") is not None


def test_area_is_real(valid_square):
    assert valid_square.area == valid_square.side ** 2


def test_perimeter_is_real(valid_square):
    assert valid_square.perimeter == valid_square.side * 4


def test_is_figure(valid_square):
    assert isinstance(valid_square, Figure)
