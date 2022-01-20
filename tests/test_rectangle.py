import pytest

from src.customexceptions import NotValidFigure
from src.figure import Figure
from src.rectangle import Rectangle


@pytest.fixture
def valid_rectangle():
    return Rectangle(10, 12)


def test_valid_rectangle(valid_rectangle):
    assert valid_rectangle is not None, "прямоугольник не создаётся"


def test_non_positive_sides():
    with pytest.raises(NotValidFigure):
        Rectangle(-10, -12)


def test_parse_to_float_sides():
    assert Rectangle("3.14", "3.16") is not None


def test_not_parse_to_float():
    with pytest.raises(ValueError):
        Rectangle("Ghbdfa", "ghdfal")


def test_area_is_real(valid_rectangle):
    assert valid_rectangle.area == valid_rectangle.side1 * valid_rectangle.side2


def test_perimeter_is_real(valid_rectangle):
    assert valid_rectangle.perimeter == (valid_rectangle.side1 + valid_rectangle.side2) * 2


def test_is_figure(valid_rectangle):
    assert isinstance(valid_rectangle, Figure)