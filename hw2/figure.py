class Figure:
    def __init__(self, name: str):
        pass

    def add_area(self, d):
        added_area = self.area() + d.area()
        return added_area
