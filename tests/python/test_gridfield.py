import unittest
import numpy as np
import rasterio
from dtcc_model.gridfield import GridField2D


class TestGridField(unittest.TestCase):
    def test_empty_gridfield(self):
        gridfield = GridField2D()
        self.assertEqual(gridfield.grid.shape, (0, 2))
        self.assertEqual(
            gridfield.transform, rasterio.Affine(1.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        )
        self.assertEqual(gridfield.cell_size, (1, 1))
        self.assertEqual(gridfield.origin, (0, 0))
