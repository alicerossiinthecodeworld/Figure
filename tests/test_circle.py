import math
import pytest

from src.circle import Circle
from src.customexceptions import NotValidFigure
from src.figure import Figure


@pytest.fixture
def valid_circle():
    return Circle(10)


def test_valid_circle(valid_circle):
    assert valid_circle is not None, "круг не создаётся"


def test_not_positive_radius():
    with pytest.raises(NotValidFigure):
        Circle(-1)


def test_not_parse_to_float_radius():
    with pytest.raises(ValueError):
        Circle("Ghbdfa")


def test_parse_to_float_radius():
    assert Circle("3.14") is not None


def test_area_is_real(valid_circle):
    assert valid_circle.area == math.pi * (valid_circle.radius ** 2)


def test_perimeter_is_real(valid_circle):
    assert valid_circle.perimeter == 2 * math.pi * valid_circle.radius


def test_is_figure(valid_circle):
    assert isinstance(valid_circle, Figure)

