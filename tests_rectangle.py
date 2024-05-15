import unittest
import rectangle
class RectangleTestCase(unittest.TestCase):
    def test_area_positive_values(self):
        res = rectangle.area(10,2)
        self.assertEqual(res,20)
    def test_area_zero_value(self):
        with self.assertRaises(ValueError):
            res = rectangle.area(0,1)
    def test_area_negative_value(self):
        with self.assertRaises(ValueError):
            res = rectangle.area(-1,1)
    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            res = rectangle.area("asd", 1)
    def test_perimeter_positive_values(self):
        res = rectangle.perimeter(10,2)
        self.assertEqual(res,24)
    def test_perimeter_zero_value(self):
        with self.assertRaises(ValueError):
            res = rectangle.perimeter(0,1)
    def test_perimeter_negative_value(self):
        with self.assertRaises(ValueError):
            res = rectangle.perimeter(-1,1)
    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            res = rectangle.perimeter("asd",1)