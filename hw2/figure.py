import sys, os

class Figure:
    def __init__(self, name: str):
        pass

    def add_area(self, d):
        sys.stdout = open(os.devnull, 'w')
        added_area = self.area() + d
        sys.stdout = sys.__stdout__
        return added_area
