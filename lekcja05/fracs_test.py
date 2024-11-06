import unittest
import fracs


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(fracs.add_frac([-1, 2], [1, 2]), [0, 1])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([4, 3], [1, 3]), [1, 1])
        self.assertEqual(fracs.sub_frac([1, 3], [1, 2]), [-1, 6])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac([1, 2], [1, 2]), [1, 4])
        self.assertEqual(fracs.mul_frac([0, 2], [21, 2]), self.zero)

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac([1, 2], [3, 2]), [1, 3])
        with self.assertRaises(ValueError):
            fracs.div_frac([1, 2], [0, 1])

    def test_is_positive(self):
        self.assertTrue(fracs.is_positive([1, 2]))
        self.assertFalse(fracs.is_positive([-1, 2]))

    def test_is_zero(self):
        self.assertTrue(fracs.is_zero([0, 1]))
        self.assertFalse(fracs.is_zero([1, 2]))

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac([1, 2], [1, 2]), 0)
        self.assertEqual(fracs.cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(fracs.cmp_frac([1, 3], [1, 2]), -1)

    def test_frac2float(self):
        self.assertEqual(fracs.frac2float([1, 2]), 0.5)
        self.assertEqual(fracs.frac2float([1, 4]), 0.25)
        self.assertAlmostEqual(fracs.frac2float([1, 3]), 0.33333333)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
