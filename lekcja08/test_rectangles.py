import pytest
from lekcja06.points import Point
from rectangles import Rectangle


@pytest.fixture
def rectangles():
    r1 = Rectangle(0, 0, 3, 2)
    r2 = Rectangle(1, 1, 5, 4)
    r3 = Rectangle(0, 0, 3, 2)
    return r1, r2, r3


def test_str(rectangles):
    r1, r2, r3 = rectangles
    assert str(r1) == "[(0, 0), (3, 2)]"
    assert str(r2) == "[(1, 1), (5, 4)]"
    assert str(r3) == str(r1)


def test_repr(rectangles):
    r1, r2, r3 = rectangles
    assert repr(r1) == "Rectangle(0, 0, 3, 2)"
    assert repr(r2) == "Rectangle(1, 1, 5, 4)"
    assert repr(r3) == repr(r1)


def test_eq(rectangles):
    r1, r2, r3 = rectangles
    assert r1 == r3


def test_ne(rectangles):
    r1, r2, r3 = rectangles
    assert r1 != r2


def test_center(rectangles):
    r1, r2, r3 = rectangles
    assert r1.center == Point(1.5, 1)
    assert r2.center == Point(3, 2.5)


def test_area(rectangles):
    r1, r2, r3 = rectangles
    assert r1.area == 6
    assert r2.area == 12


def test_move(rectangles):
    r1, r2, r3 = rectangles
    r1.move(1, 1)
    assert r1 == Rectangle(1, 1, 4, 3)
    r2.move(-1, -1)
    assert r2 == Rectangle(0, 0, 4, 3)


def test_intersection(rectangles):
    r1, r2, r3 = rectangles
    assert r1.intersection(r2) == Rectangle(1, 1, 3, 2)
    assert r1.intersection(r3) == r1


def test_cover(rectangles):
    r1, r2, r3 = rectangles
    assert r1.cover(r2) == Rectangle(0, 0, 5, 4)
    assert r1.cover(r3) == r1


def test_make4(rectangles):
    r1, r2, r3 = rectangles
    parts = r1.make4()
    assert parts[0] == Rectangle(0, 0, 1.5, 1)
    assert parts[1] == Rectangle(1.5, 0, 3, 1)
    assert parts[2] == Rectangle(0, 1, 1.5, 2)
    assert parts[3] == Rectangle(1.5, 1, 3, 2)


def test_virtual_attributes(rectangles):
    r1, r2, r3 = rectangles
    assert r1.top == 2
    assert r1.bottom == 0
    assert r1.left == 0
    assert r1.right == 3
    assert r1.width == 3
    assert r1.height == 2
    assert r1.topleft == Point(0, 2)
    assert r1.bottomleft == Point(0, 0)
    assert r1.topright == Point(3, 2)
    assert r1.bottomright == Point(3, 0)
