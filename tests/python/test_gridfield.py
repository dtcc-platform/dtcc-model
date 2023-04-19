import unittest
import numpy as np
import affine
from dtcc_model.gridfield import GridField2D


class TestGridField(unittest.TestCase):
    def test_empty_gridfield(self):
        gridfield = GridField2D()
        self.assertEqual(gridfield.grid.shape, (0, 2))
        self.assertEqual(
            gridfield.transform, affine.Affine(1.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        )
        self.assertEqual(gridfield.cell_size, (1, 1))
        self.assertEqual(gridfield.origin, (0, 0))

    def test_gridfield_bounds(self):
        data = np.arange(10 * 20).reshape(10, 20)
        gridfield = GridField2D(data, affine.Affine(2, 0, 0, 0, -2, 0), "EPSG:3857")
        self.assertEqual(gridfield.bounds, (0, -40, 20, 0))

    def test_to_protobuf(self):
        data = np.arange(10 * 20).reshape(10, 20)
        gridfield = GridField2D(data, affine.Affine(2, 0, 0, 0, -2, 0), "EPSG:3857")
        proto = gridfield.to_proto()
        self.assertEqual(proto.grid.xSize, gridfield.width)
        self.assertEqual(proto.grid.ySize, gridfield.height)
        self.assertEqual(proto.grid.xStep, gridfield.cell_size[0])
        self.assertEqual(proto.grid.yStep, gridfield.cell_size[1])
        self.assertEqual(proto.grid.boundingBox.p.x, gridfield.bounds[0])
        self.assertEqual(proto.grid.boundingBox.p.y, gridfield.bounds[1])
        self.assertEqual(proto.grid.boundingBox.q.x, gridfield.bounds[2])
        self.assertEqual(proto.grid.boundingBox.q.y, gridfield.bounds[3])
        self.assertEqual(proto.values, data.flatten().tolist())

    def test_from_protobuf(self):
        data = np.arange(10 * 20).reshape(10, 20)
        gridfield = GridField2D(data, affine.Affine(2, 0, 0, 0, -2, 0), "EPSG:3857")
        proto = gridfield.to_proto()
        gridfield2 = GridField2D()
        gridfield2.from_proto(proto)
        self.assertEqual(gridfield2.grid.shape, gridfield.grid.shape)
        self.assertEqual(gridfield2.transform, gridfield.transform)
        self.assertEqual(gridfield2.cell_size, gridfield.cell_size)
        self.assertEqual(gridfield2.origin, gridfield.origin)
        self.assertEqual(gridfield2.bounds, gridfield.bounds)
        self.assertEqual(gridfield2.grid.tolist(), gridfield.grid.tolist())
