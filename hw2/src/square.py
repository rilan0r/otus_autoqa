from hw2.figure import Figure


class Square(Figure):
    def __init__(self, a):
        if not isinstance(a, (float, int)):
            raise ValueError(f"{a} is not a digit")
        if a < 0:
            raise ValueError(f"{a} is lesser then 0")
        self.a = a

    def perimeter(self):
        perimeter = self.a * 4
        return perimeter

    def area(self):
        area = self.a ** 2
        return area
