from hw2.figure import Figure
import math


class Circle(Figure):
    def __init__(self, r):
        if not isinstance(r, float) and not isinstance(r, int):
            raise ValueError(f"{r} is not a digit")
        if (isinstance(r, float) or isinstance(r, int)) and r < 0:
            raise ValueError(f"{r} is lesser then 0")
        self.R = r

    def perimeter(self):
        perimeter = self.R * 2 * math.pi
        return perimeter

    def area(self):
        area = math.pi * (self.R ** 2)
        return area
