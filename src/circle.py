import math

from src.figure import Figure
from src.customexceptions import NotValidFigure


class Circle(Figure):
    NAME = "Circle"

    def __init__(self, radius):
        fl_radius = self._float_number(radius)
        if self._is_valid(fl_radius):
            self.radius = fl_radius
            super().__init__()
        else:
            raise NotValidFigure

    def _is_valid(self, radius):
        return radius > 0

    def _get_perimeter(self):
        return 2 * math.pi * self.radius

    def _get_area(self):
        return math.pi * (self.radius ** 2)
