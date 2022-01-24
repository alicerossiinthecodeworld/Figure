import pytest
from src.figure import Figure
from tests.test_triangle import valid_triangle
from tests.test_square import valid_square


def test_can_not_create_figure():
    with pytest.raises(TypeError):
        Figure()


def test_can_add_area(valid_triangle, valid_square):
    assert valid_triangle.add_area(valid_square) == valid_triangle.area + valid_square.area