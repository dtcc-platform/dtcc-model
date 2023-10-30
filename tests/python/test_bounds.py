import unittest
from dtcc_model.geometry import Bounds


class TestBounds(unittest.TestCase):
    def test_create(self):
        bounds = Bounds(1, 2, 3, 4)
        self.assertEqual(bounds.xmin, 1)
        self.assertEqual(bounds.ymin, 2)
        self.assertEqual(bounds.xmax, 3)
        self.assertEqual(bounds.ymax, 4)

    def test_area(self):
        bounds = Bounds(0, 0, 10, 10)
        self.assertEqual(bounds.area, 100)

    def test_buffer(self):
        bounds = Bounds(0, 0, 10, 10)
        bounds.buffer(1)
        self.assertEqual(bounds.xmin, -1)
        self.assertEqual(bounds.ymin, -1)
        self.assertEqual(bounds.xmax, 11)
        self.assertEqual(bounds.ymax, 11)

    def test_union(self):
        bounds = Bounds(0, 0, 10, 10)
        bounds.union(Bounds(5, 5, 15, 15))
        self.assertEqual(bounds.xmin, 0)
        self.assertEqual(bounds.ymin, 0)
        self.assertEqual(bounds.xmax, 15)
        self.assertEqual(bounds.ymax, 15)

    def test_intersection(self):
        bounds = Bounds(0, 0, 10, 10)
        bounds.intersect(Bounds(5, 5, 15, 15))
        self.assertEqual(bounds.xmin, 5)
        self.assertEqual(bounds.ymin, 5)
        self.assertEqual(bounds.xmax, 10)
        self.assertEqual(bounds.ymax, 10)


if __name__ == "__main__":
    unittest.main()
