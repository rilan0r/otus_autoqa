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
        self.a = a
        self.b = b
        self.c = c
        if (a + b < c) or (a + c < b) or (b + c < a):
            raise ValueError('Sorry, but such triangle is impossible')

    def perimeter(self):
        perimeter = (self.a + self.b + self.c)
        return perimeter

    def area(self):
        half_perimeter = self.perimeter() / 2
        area = math.sqrt(half_perimeter * (half_perimeter - self.a) *
                         (half_perimeter - self.b) * (half_perimeter - self.c))
        return area


triangle = Triangle(3,4,5)
triangle2 = Triangle(30, 40, 50)
print(triangle.area())
total_area = triangle.add_area(triangle2)
print(total_area)
