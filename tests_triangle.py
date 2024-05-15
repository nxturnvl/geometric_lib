import unittest
import triangle
class TriangleTestCase(unittest.TestCase):
    def test_area_positive_values(self):
        res = triangle.area(10,2)
        self.assertEqual(res,10)
    def test_area_zero_value(self):
        with self.assertRaises(ValueError):
            res = triangle.area(0,1)
    def test_area_negative_value(self):
        with self.assertRaises(ValueError):
            res = triangle.area(-1,1)
    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            res = triangle.area("asd", 1)
    def test_perimeter_positive_values(self):
        res = triangle.perimeter(1,2,3)
        self.assertEqual(res,6)
    def test_perimeter_zero_value(self):
        with self.assertRaises(ValueError):
            res = triangle.perimeter(0,1,2)
    def test_perimeter_negative_value(self):
        with self.assertRaises(ValueError):
            res = triangle.perimeter(-1,1,2)
    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            res = triangle.perimeter("asd",1,2)