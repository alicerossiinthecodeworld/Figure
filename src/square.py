from src.customexceptions import NotValidFigure
from src.figure import Figure


class Square(Figure):
    def __init__(self, side):
        fl_side = self._float_number(side)
        if self._is_valid(fl_side):
            self.side = fl_side
            super().__init__()
        else:
            raise NotValidFigure

    def _is_valid(self, side):
        return side > 0

    def _get_area(self):
        return self.side ** 2

    def _get_perimeter(self):
        return self.side * 4
