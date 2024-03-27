import unittest
from shapely.geometry import Polygon
import numpy as np
from dtcc_model import Surface, MultiSurface


class TestSurface(unittest.TestCase):

    def test_convert_polygon(self):
        s = Surface()
        s.from_polygon(Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]), 10)
        v1 = s.vertices[1]
        self.assertEqual(len(s.vertices), 4)
        self.assertEqual(v1[0], 1)
        self.assertEqual(v1[1], 0)
        self.assertEqual(v1[2], 10)
        self.assertEqual(s.zmax, 10)

    def test_to_polygon(self):
        s = Surface()
        s.from_polygon(Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]), 10)
        p = s.to_polygon()

        self.assertEqual(len(p.exterior.coords), 4 + 1)
        self.assertEqual(list(p.exterior.coords)[0], (0, 0))
        self.assertEqual(list(p.exterior.coords)[1], (1, 0))
        self.assertEqual(list(p.exterior.coords)[2], (1, 1))
        self.assertEqual(list(p.exterior.coords)[3], (0, 1))

    def test_to_proto(self):
        verts = np.array([[0, 0, 10], [1, 0, 10], [1, 1, 12], [0, 1, 12]])
        hole = np.array(
            [[0.1, 0.1, 10], [0.9, 0.1, 10], [0.9, 0.9, 12], [0.1, 0.9, 12]]
        )
        s = Surface(vertices=verts, holes=[hole])
        pb = s.to_proto()
        self.assertEqual(len(pb.surface.vertices), 4 * 3)
        self.assertEqual(pb.surface.vertices[0], 0)
        self.assertEqual(pb.surface.vertices[-1], 12)
        self.assertEqual(len(pb.surface.holes), 1)

    def test_from_proto(self):
        verts = np.array([[0, 0, 10], [1, 0, 10], [1, 1, 12], [0, 1, 12]])
        hole = np.array(
            [[0.1, 0.1, 10], [0.9, 0.1, 10], [0.9, 0.9, 12], [0.1, 0.9, 12]]
        )
        s = Surface(vertices=verts, holes=[hole])
        pb = s.to_proto()
        pb = pb.SerializeToString()

        s2 = Surface()
        s2.from_proto(pb)

        self.assertEqual(len(s2.vertices), 4)
        self.assertEqual(len(s2.holes), 1)
        self.assertListEqual(list(s2.vertices[0]), [0, 0, 10])
        self.assertListEqual(list(np.round(s2.holes[0][2], 6)), [0.9, 0.9, 12])


class TestMultiSurface(unittest.TestCase):

    def test_zmax(self):
        s1 = Surface(vertices=np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0]]))
        s2 = Surface(vertices=np.array([[0, 0, 1], [1, 0, 1], [1, 1, 2]]))
        ms = MultiSurface(surfaces=[s1, s2])
        self.assertEqual(ms.zmax, 2)

    def test_to_proto(self):
        s1 = Surface(vertices=np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0]]))
        s2 = Surface(vertices=np.array([[0, 0, 1], [1, 0, 1], [1, 1, 2]]))
        ms = MultiSurface(surfaces=[s1, s2])
        pb = ms.to_proto()
        self.assertEqual(len(pb.multi_surface.surfaces), 2)

    def test_from_proto(self):
        s1 = Surface(vertices=np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0]]))
        s2 = Surface(vertices=np.array([[0, 0, 1], [1, 0, 1], [1, 1, 2]]))
        ms = MultiSurface(surfaces=[s1, s2])
        pb = ms.to_proto()
        pb = pb.SerializeToString()

        ms2 = MultiSurface()
        ms2.from_proto(pb)

        self.assertEqual(len(ms2.surfaces), 2)
        self.assertEqual(ms2.zmax, 2)


if __name__ == "__main__":
    unittest.main()
