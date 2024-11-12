import unittest
import rectangles as r
from lekcja06.rectangles import Rectangle


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.r1 = r.Rectangle(0, 0, 3, 2)
        self.r2 = r.Rectangle(1, 1, 5, 4)
        self.r3 = r.Rectangle(0, 0, 3, 2)

    def test_str(self):
        self.assertEqual(str(self.r1), "[(0, 0), (3, 2)]")
        self.assertEqual(str(self.r2), "[(1, 1), (5, 4)]")

    def test_repr(self):
        self.assertEqual(repr(self.r1), "Rectangle(0, 0, 3, 2)")
        self.assertEqual(repr(self.r2), "Rectangle(1, 1, 5, 4)")

    def test_eq(self):
        self.assertEqual(self.r1, self.r3)
        self.assertNotEqual(self.r1, self.r2)

    def test_ne(self):
        self.assertNotEqual(self.r1, self.r2)

    def test_center(self):
        self.assertEqual(self.r1.center(), r.Point(3 / 2, 1))
        self.assertEqual(self.r2.center(), r.Point(3, 5 / 2))

    def test_area(self):
        self.assertEqual(self.r1.area(), 6)
        self.assertEqual(self.r2.area(), 12)

    def test_move(self):
        self.r1.move(1, 1)
        self.assertEqual(self.r1, Rectangle(1, 1, 4, 3))
        self.r2.move(-1, -1)
        self.assertEqual(self.r2, Rectangle(0, 0, 4, 3))


if __name__ == '__main__':
    unittest.main()
