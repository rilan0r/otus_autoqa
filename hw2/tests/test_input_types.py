import pytest

from hw2.src.square import Square
from hw2.src.circle import Circle
from hw2.src.rectangle import Rectangle
from hw2.src.triangle import Triangle


def test_digits_square():
    test = Square(1)
    test2 = Square(1.0)
    with pytest.raises(ValueError, match='is not a digit'):
        test3 = Square('test')


def test_floats_rectangle():
    test = Rectangle(1, 1)
    test2 = Rectangle(1.0, 1.0)
    with pytest.raises(ValueError, match='is not a digit'):
        test3 = Rectangle('test', 'test')


def test_floats_triangle():
    test = Triangle(1, 1, 1)
    test2 = Triangle(1.0, 1.0, 1.0)
    with pytest.raises(ValueError, match='is not a digit'):
        test3 = Triangle('test', 'test', 'test')


def test_floats_circle():
    test = Circle(1)
    test2 = Circle(1.0)
    with pytest.raises(ValueError, match='is not a digit'):
        test3 = Circle('test')
