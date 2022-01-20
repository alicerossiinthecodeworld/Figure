from src.customexceptions import NotValidFigure
from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side1, side2):
        fl_side1 = self._float_number(side1)
        fl_side2 = self._float_number(side2)
        if self._is_valid(fl_side1, fl_side2):
            self.side1 = fl_side1
            self.side2 = fl_side2
            super().__init__()
        else:
            raise NotValidFigure

    def _is_valid(self, side1, side2):
        return side1 > 0 and side2 > 0

    def _get_perimeter(self):
        return (self.side1 + self.side2) * 2

    def _get_area(self):
        return self.side1 * self.side2
