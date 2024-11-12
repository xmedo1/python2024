import math
import unittest
import points as p


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.p1 = p.Point(1, 2)
        self.p2 = p.Point(3, 4)
        self.p3 = p.Point(1, 2)
        self.zero = p.Point(0, 0)

    def test_str(self):
        self.assertEqual(str(self.p1), "(1, 2)")
        self.assertEqual(str(self.p2), "(3, 4)")
        self.assertEqual(str(self.zero), "(0, 0)")

    def test_repr(self):
        self.assertEqual(repr(self.p1), "Point(1, 2)")
        self.assertEqual(repr(self.p3), "Point(1, 2)")
        self.assertEqual(repr(self.zero), "Point(0, 0)")

    def test_eq(self):
        self.assertEqual(self.p1, self.p3)

    def test_ne(self):
        self.assertNotEqual(self.p1, self.p2)

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, p.Point(4, 6))
        self.assertEqual(self.p1 + self.zero, self.p1)
        self.assertEqual(self.p1 + self.p3, p.Point(2, 4))

    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, p.Point(-2, -2))
        self.assertEqual(self.p1 - self.zero, self.p1)
        self.assertEqual(self.p1 - self.p3, self.zero)

    def test_mul(self):
        self.assertEqual(self.p1 * self.p2, 11)
        self.assertEqual(self.p1 * self.zero, 0)
        self.assertEqual(self.p1 * self.p3, 5)

    def test_cross(self):
        self.assertEqual(self.p1.cross(self.p3), 0)
        self.assertEqual(self.p1.cross(self.p2), -2)

    def test_length(self):
        self.assertEqual(self.p1.length(), math.sqrt(5))
        self.assertEqual(self.zero.length(), 0)
        self.assertEqual(self.p2.length(), 5)

    def test_hash(self):
        self.assertEqual(hash(self.p1), hash(self.p3))
        self.assertNotEqual(hash(self.p1), hash(self.p2))


if __name__ == '__main__':
    unittest.main()
