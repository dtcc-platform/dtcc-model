import unittest

from dtcc_model.pointcloud import Pointcloud


class TestPointcloud(unittest.TestCase):
    def test_empty(self):
        pc = Pointcloud()
        self.assertEqual(pc.points.shape[1], 3)
        self.assertEqual(pc.crs, "")
        self.assertEqual(pc.origin, (0, 0))
        self.assertEqual(pc.bounds, (0, 0, 0, 0))

    def test_from_proto(self):
        pass

    def test_to_proto(self):
        pass
