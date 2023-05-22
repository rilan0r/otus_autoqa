class Figure:
    def __init__(self, name: str):
        pass

    def add_area(self, figure):
        added_area = self.area() + figure.area()
        return added_area
