import unittest
import square
class SquareTestCase(unittest.TestCase):
    def test_area_positive_value(self):
        res = square.area(10)
        self.assertEqual(res,100)
    def test_area_zero_value(self):
        with self.assertRaises(ValueError):
            res = square.area(0)
    def test_area_negative_value(self):
        with self.assertRaises(ValueError):
            res = square.area(-1)
    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            res = square.area("asd")
    def test_perimeter_positive_value(self):
        res = square.perimeter(10)
        self.assertEqual(res,40)
    def test_perimeter_zero_value(self):
        with self.assertRaises(ValueError):
            res = square.perimeter(0)
    def test_perimeter_negative_value(self):
        with self.assertRaises(ValueError):
            res = square.perimeter(-1)
    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            res = square.perimeter("asd")
