from hw2.figure import Figure
import math


class Circle(Figure):
    def __init__(self, r):
        if not isinstance(r, (float, int)):
            raise ValueError(f"{r} is not a digit")
        if r < 0:
            raise ValueError(f"{r} is lesser then 0")
        self.r = r

    def perimeter(self):
        perimeter = self.r * 2 * math.pi
        return perimeter

    def area(self):
        area = math.pi * (self.r ** 2)
        return area
