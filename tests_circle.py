import math
import unittest
import circle
class CircleTestCase(unittest.TestCase):
    def test_area_positive_value(self):
        res = circle.area(3)
        self.assertEqual(res,3 * 3 * math.pi)
    def test_area_zero_value(self):
        with self.assertRaises(ValueError):
            res = circle.area(0)
    def test_area_negative_value(self):
        with self.assertRaises(ValueError):
            res = circle.area(-1)
    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            res = circle.area("asd")

    def test_perimeter_positive_value(self):
        res = circle.perimeter(3)
        self.assertEqual(res,2 * 3 * math.pi)
    def test_perimeter_zero_value(self):
        with self.assertRaises(ValueError):
            res = circle.perimeter(0)
    def test_perimeter_negative_value(self):
        with self.assertRaises(ValueError):
            res = circle.perimeter(-1)
    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            res = circle.perimeter("asd")