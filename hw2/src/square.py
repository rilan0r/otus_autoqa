from hw2.figure import Figure


class Square(Figure):
    def __init__(self, a):
        if not isinstance(a, float) and not isinstance(a, int):
            raise ValueError(f"{a} is not a digit")
        if a < 0:
            raise ValueError(f"{a} is lesser then 0")
        self.A = a

    def perimeter(self):
        perimeter = self.A * 4
        return perimeter

    def area(self):
        area = self.A ** 2
        return area