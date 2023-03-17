import unittest
import dtcc_model


class TestPolygon(unittest.TestCase):

    def test_linear_ring(self):
        lr = dtcc_model.LinearRing()
        vertices = []
        for c in [(0, 0), (1, 0), (1, 1), (0, 1)]:
            v = dtcc_model.Vector2D()
            v.x = c[0]
            v.y = c[1]
            vertices.append(v)
        lr.vertices.extend(vertices)
        self.assertEqual(lr.vertices[2].x, 1)
        self.assertEqual(lr.vertices[2].y, 1)

    def test_polygon(self):
        p = dtcc_model.Polygon()
        lr = dtcc_model.LinearRing()
        vertices = []
        for c in [(0, 0), (1, 0), (1, 1), (0, 1)]:
            v = dtcc_model.Vector2D()
            v.x = c[0]
            v.y = c[1]
            vertices.append(v)
        lr.vertices.extend(vertices)
        p.shell.CopyFrom(lr)
        self.assertEqual(p.shell.vertices[2].x, 1)
        self.assertEqual(p.shell.vertices[2].y, 1)
