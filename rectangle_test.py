import unittest
from ejercicio2_rectangle import Rectangle
from ejercicio2_point import Point

class TestRectangle(unittest.TestCase):
    def test_area(self):
        # Test case 1: Rectangle with points (0, 0) and (3, 4)
        rect1 = Rectangle(Point(0, 0), Point(3, 4))
        self.assertEqual(rect1.area, 12)

        # Test case 2: Rectangle with points (-1, -1) and (2, 3)
        rect2 = Rectangle(Point(-1, -1), Point(2, 3))
        self.assertEqual(rect2.area, 12)

        # Test case 3: Rectangle with points (-2, 0) and (2, 4)
        rect3 = Rectangle(Point(-2, 0), Point(2, 4))
        self.assertEqual(rect3.area, 8)

    def test_perimeter(self):
        # Test case 1: Rectangle with points (0, 0) and (3, 4)
        rect1 = Rectangle(Point(0, 0), Point(3, 4))
        self.assertEqual(rect1.perimeter, 14)

        # Test case 2: Rectangle with points (-1, -1) and (2, 3)
        rect2 = Rectangle(Point(-1, -1), Point(2, 3))
        self.assertEqual(rect2.perimeter, 14)

        # Test case 3: Rectangle with points (-2, 0) and (2, 4)
        rect3 = Rectangle(Point(-2, 0), Point(2, 4))
        self.assertEqual(rect3.perimeter, 12)

if __name__ == '__main__':
    unittest.main()
