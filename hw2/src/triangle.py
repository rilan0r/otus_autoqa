from hw2.figure import Figure
import math


class Triangle(Figure):
    def __init__(self, a, b, c):
        if not isinstance(a, float) and not isinstance(a, int):
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

    def type(self):
        return


triangle = Triangle(3, 4, 5)
triangle2 = Triangle(100, 120, 160)
area1 = float(("{:.2f}".format(triangle.area())))
perimeter1 = float(("{:.2f}".format(triangle.perimeter())))
area2 = float(("{:.2f}".format(triangle2.area())))
perimeter2 = float(("{:.2f}".format(triangle2.perimeter())))
area_total = float(("{:.2f}".format(triangle.add_area(area2))))
print(f"Area of 1st figure is {area1}")
print(f"Area of 2nd figure is {area2}")
print(f"Perimeter of 1st figure is {perimeter1}")
print(f"Perimeter of 2nd figure is {perimeter2}")
print(f"Total area of 2 figures is {area_total}")
