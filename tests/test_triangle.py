import pytest

from src.customexceptions import NotValidFigure
from src.figure import Figure
from src.triangle import Triangle


@pytest.fixture
def valid_triangle():
    return Triangle(3, 4, 5)


def test_valid_triangle(valid_triangle):
    assert valid_triangle is not None, "треугольник не создаётся"


def test_impossible_triangle():
    with pytest.raises(NotValidFigure):
        Triangle(-3, -4, -5)


def test_not_parse_to_float_side():
    with pytest.raises(ValueError):
        Triangle(3, 4, "ghbjfdga")


def test_parse_to_float_sides():
    assert Triangle("3.14", 4, 5) is not None


def test_area_is_real(valid_triangle):
    p = valid_triangle.perimeter / 2
    assert valid_triangle.area == (
                p * (p - valid_triangle.side1) * (p - valid_triangle.side2) * (p - valid_triangle.side3)) ** 0.5


def test_perimeter_is_real(valid_triangle):
    assert valid_triangle.perimeter == valid_triangle.side1 + valid_triangle.side2 + valid_triangle.side3


def test_is_figure(valid_triangle):
    assert isinstance(valid_triangle, Figure)

