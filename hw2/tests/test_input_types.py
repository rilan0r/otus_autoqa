import pytest

from hw2.src.square import Square
from hw2.src.circle import Circle
from hw2.src.rectangle import Rectangle
from hw2.src.triangle import Triangle


def test_digits_square_positive():
    test = Square(1)
    assert test.area() == 1
    assert test.perimeter() == 4
    test2 = Square(1.0)
    assert test2.area() == 1
    assert test2.perimeter() == 4


def test_digits_square_negative():
    with pytest.raises(ValueError, match='is not a digit'):
        test = Square('test')


def test_floats_rectangle_positive():
    test = Rectangle(1, 1)
    assert test.area() == 1
    assert test.perimeter() == 4
    test2 = Rectangle(1.0, 1.0)
    assert test2.area() == 1
    assert test2.perimeter() == 4

@pytest.mark.parametrize(
    "a, b",
    [
        (1, 'test'),
        ('test', 1)
    ]
)
def test_floats_rectangle_negative(a, b):
    with pytest.raises(ValueError, match='is not a digit'):
        test = Rectangle(a, b)


def test_floats_triangle_positive():
    test = Triangle(3, 4, 5)
    assert test.area() == 6
    assert test.perimeter() == 12
    test2 = Triangle(3.0, 4.0, 5.0)
    assert test2.area() == 6
    assert test2.perimeter() == 12


@pytest.mark.parametrize(
    "a, b, c",
    [
        ('test', 1, 1),
        (1, 'test', 1),
        (1, 1, 'test')
    ]
)
def test_floats_triangle_negative(a, b, c):
    with pytest.raises(ValueError, match='is not a digit'):
        test = Triangle('test', 'test', 'test')


def test_floats_circle_positive():
    test = Circle(2567)
    assert int(test.area()) == 20701490
    assert int(test.perimeter()) == 16128
    test2 = Circle(2567.0)
    assert int(test2.area()) == 20701490
    assert int(test2.perimeter()) == 16128


def test_floats_circle_negative():
    with pytest.raises(ValueError, match='is not a digit'):
        test = Circle('test')

def test_added_area_is_a_figure():
    with pytest.raises(AttributeError, match='object has no attribute \'area\''):
        triangle = Triangle(3, 4, 5)
        test = triangle.add_area(10)
    test = Triangle(3, 4, 5)
    test2 = Triangle(30, 40, 50)
    if test.add_area(test2) != 606:
        pytest.raises(ValueError, "Added area counts wrong!")
