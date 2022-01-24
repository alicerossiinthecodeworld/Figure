from src.figure import Figure
from src.customexceptions import NotValidFigure


class Triangle(Figure):
    NAME = "Triangle"

    def __init__(self, side1, side2, side3):
        fl_side1 = self._float_number(side1)
        fl_side2 = self._float_number(side2)
        fl_side3 = self._float_number(side3)
        if self._is_valid(fl_side1, fl_side2, fl_side3):
            self.side1 = fl_side1
            self.side2 = fl_side2
            self.side3 = fl_side3
            super().__init__()
        else:
            raise NotValidFigure

    @staticmethod
    def _is_valid(side1, side2, side3):
        return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1

    @classmethod
    def create_with_validation(cls, side1, side2, side3):
        try:
            cls(side1, side2, side3)
        except TypeError:
            print("В конструктор пришло не число!")
        except NotValidFigure:
            print("Не валидная фигура")

    def _get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def _get_area(self):
        p = self._get_perimeter() / 2  # расчет полупериметра
        return (p * (p - self.side1) * (p - self.side2) * (p - self.side3)) ** 0.5  # расчет площади по формуле Герона
