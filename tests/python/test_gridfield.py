import unittest
import numpy as np
import affine
from dtcc_model.gridfields import GridField


class TestGridField(unittest.TestCase):
    def test_empty_gridfield(self):
        gridfield = GridField()
        self.assertEqual(len(gridfield.values), 0)
        self.assertEqual(gridfield.grid.bounds.tuple, (0, 0, 0, 0))
