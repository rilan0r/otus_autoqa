from hw2.figure import Figure
import math


class Triangle(Figure):
    def __init__(self, a, b, c):
        if not isinstance(a, (float, int)):
            raise ValueError(f"{a} is not a digit")
        if not isinstance(b, float) and not isinstance(b, int):
            raise ValueError(f"{b} is not a digit")
        if not isinstance(c, float) and not isinstance(c, int):
            raise ValueError(f"{c} is not a digit")
        if a < 0:
            raise ValueError(f"{a} is lesser then 0")
        if b < 0:
            raise ValueError(f"{b} is lesser then 0")
        if c < 0:
            raise ValueError(f"{c} is lesser then 0")
        self.A = a
        self.B = b
        self.C = c
        if (a + b < c) or (a + c < b) or (b + c < a):
            raise ValueError('Sorry, but such triangle is impossible')

    def perimeter(self):
        perimeter = (self.A + self.B + self.C)
        return perimeter

    def area(self):
        perimeter = Triangle.perimeter(self)
        area = math.sqrt(perimeter * (perimeter - self.A) * (perimeter - self.B) * (perimeter - self.C))
        return area
