import math
import unittest

import circle
import rectangle
import square


class SquareTestCase(unittest.TestCase):
    def test_area_usual(self):
        self.assertEqual(square.area(5), 25)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(square.area(1.5), 2.25)

    def test_perimeter_usual(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_float(self):
        self.assertAlmostEqual(square.perimeter(1.5), 6.0)


class CircleTestCase(unittest.TestCase):
    def test_area_usual(self):
        self.assertAlmostEqual(circle.area(3), 28.274333882308138)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_unit_radius(self):
        self.assertAlmostEqual(circle.area(1), math.pi)

    def test_perimeter_usual(self):
        self.assertAlmostEqual(circle.perimeter(3), 18.84955592153876)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_unit_radius(self):
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)


class RectangleTestCase(unittest.TestCase):
    def test_area_usual(self):
        self.assertEqual(rectangle.area(3, 4), 13)

    def test_area_zero(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_area_square(self):
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_perimeter_usual(self):
        self.assertEqual(rectangle.perimeter(3, 4), 14)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(5, 0), 10)

    def test_perimeter_square(self):
        self.assertEqual(rectangle.perimeter(10, 10), 40)


if __name__ == "__main__":
    unittest.main()