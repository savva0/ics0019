# -*- coding: utf-8 -*-
#Look at: https://docs.pytest.org/en/latest/goodpractices.html

import unittest
from quadratic_equation import quadratic_equation

class QuadraticEquationTests(unittest.TestCase):
    def test_linear_equation(self):
        self.assertEqual((-1), quadratic_equation(0, 4, 4))

    def test_d_equal_zero(self):
        self.assertEqual((-2), quadratic_equation(1, 4, 4))

    def test_d_above_zero(self):
        self.assertEqual({'x1': -0.5, 'x2': 2.0}, quadratic_equation(2, -3, -2))

    def test_d_below_zero(self):
        self.assertEqual((None), quadratic_equation(1, 2, 3))

    def test_a_b_zero(self):
        self.assertEqual((None), quadratic_equation(0, 0, 3))

if __name__ == '__main__':
    unittest.main()