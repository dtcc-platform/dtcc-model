import unittest
import numpy as np
from dtcc_model.pointcloud import PointCloud


class TestPointCloud(unittest.TestCase):
    def test_empty(self):
        pc = PointCloud()
        self.assertEqual(pc.georef.crs, "")
        self.assertEqual(pc.bounds.tuple, (0, 0, 0, 0))

    def test_calc_bounds(self):
        pc = PointCloud()
        pc.points = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
        pc.calculate_bounds()
        self.assertEqual(pc.bounds.tuple, (0, 0, 2, 2))

    def test_to_proto(self):
        pc = PointCloud()
        pc.points = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
        pc.calculate_bounds()
        pc.crs = "EPSG:3857"
        pc.origin = (0, 0)
        pc.classification = np.array([1, 2, 3])
        pc.intensity = np.array([1, 2, 3])
        pc.return_number = np.array([1, 1, 1])
        pc.num_returns = np.array([1, 1, 1])

        proto_pc = pc.to_proto()
        self.assertEqual(proto_pc.points, [0, 0, 0, 1, 1, 1, 2, 2, 2])
        self.assertEqual(proto_pc.classification, [1, 2, 3])

    def test_to_protobuf_missing_fields(self):
        pc = PointCloud()
        pc.points = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
        pc.calculate_bounds()
        proto_pc = pc.to_proto()
        self.assertEqual(proto_pc.points, [0, 0, 0, 1, 1, 1, 2, 2, 2])
        self.assertEqual(proto_pc.classification, [])

    def test_from_proto(self):
        pc = PointCloud()
        pc.points = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
        pc.calculate_bounds()
        pc.crs = "EPSG:3857"
        pc.origin = (0, 0)
        pc.classification = np.array([1, 2, 3])
        pc.intensity = np.array([1, 2, 3])
        pc.return_number = np.array([1, 1, 1])
        pc.num_returns = np.array([1, 1, 1])

        proto_pc = pc.to_proto()

        pc2 = PointCloud()
        pc2.from_proto(proto_pc)
        self.assertEqual(pc2.points.tolist(), pc.points.tolist())
        self.assertEqual(pc2.classification.tolist(), pc.classification.tolist())
