import unittest
from dtcc_model import Transform

import unittest
import numpy as np


class TestTransform(unittest.TestCase):
    def setUp(self):
        self.transform = Transform()

    def test_set_translation(self):
        self.transform.set_translation(1, 2, 3)
        expected_matrix = np.eye(4)
        expected_matrix[:3, 3] = [1, 2, 3]
        self.assertTrue(
            np.array_equal(self.transform.affine, expected_matrix),
            "Translation should be set correctly",
        )

    def test_set_rotation(self):
        rotation_matrix = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
        self.transform.set_rotation(rotation_matrix)
        expected_matrix = np.eye(4)
        expected_matrix[:3, :3] = rotation_matrix
        self.assertTrue(
            np.array_equal(self.transform.affine, expected_matrix),
            "Rotation should be set correctly",
        )

    def test_call_single_point(self):
        self.transform.set_translation(1, 2, 3)
        point = (0, 0, 0)
        transformed = self.transform(point)
        self.assertEqual(
            transformed, (1, 2, 3), "Single point should be transformed correctly"
        )

    def test_call_multiple_points(self):
        self.transform.set_translation(1, 2, 3)
        points_array = np.array([[0, 0, 0], [1, 1, 1]])
        transformed = self.transform(points_array)
        expected = np.array([[1, 2, 3], [2, 3, 4]])
        self.assertTrue(
            np.array_equal(transformed, expected),
            "Array of points should be transformed correctly",
        )


if __name__ == "__main__":
    unittest.main()
