from hw2.figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        if not isinstance(a, float) and not isinstance(a, int):
            raise ValueError(f"{a} is not a digit")
        if not isinstance(b, float) and not isinstance(b, int):
            raise ValueError(f"{b} is not a digit")
        if a < 0:
            raise ValueError(f"{a} is lesser then 0")
        if b < 0:
            raise ValueError(f"{b} is lesser then 0")
        self.A = a
        self.B = b

    def perimeter(self):
        perimeter = (self.A + self.B) * 2
        return perimeter

    def area(self):
        area = self.A * self.B
        return area
