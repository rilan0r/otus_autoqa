import pytest

from hw2.src.square import Square
from hw2.src.circle import Circle
from hw2.src.rectangle import Rectangle
from hw2.src.triangle import Triangle


def test_digits_square_positive():
    test = Square(1)
    test2 = Square(1.0)


def test_digits_square_negative():
    with pytest.raises(ValueError, match='is not a digit'):
        test = Square('test')


def test_floats_rectangle_positive():
    test = Rectangle(1, 1)
    test2 = Rectangle(1.0, 1.0)


def test_floats_rectangle_negative():
    with pytest.raises(ValueError, match='is not a digit'):
        test = Rectangle('test', 'test')


def test_floats_triangle_positive():
    test = Triangle(1, 1, 1)
    test2 = Triangle(1.0, 1.0, 1.0)


def test_floats_triangle_negative():
    with pytest.raises(ValueError, match='is not a digit'):
        test = Triangle('test', 'test', 'test')


def test_floats_circle_positive():
    test = Circle(1)
    test2 = Circle(1.0)


def test_floats_circle_negative():
    with pytest.raises(ValueError, match='is not a digit'):
        test = Circle('test')

def test_added_area_is_a_figure():
    with pytest.raises(AttributeError, match='object has no attribute \'area\''):
        triangle = Triangle(3,4,5)
        test = triangle.add_area(10)
