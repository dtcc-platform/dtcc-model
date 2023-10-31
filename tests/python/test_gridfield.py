import unittest

from dtcc_model import GridField


class TestGridField(unittest.TestCase):
    def test_empty_gridfield(self):
        gridfield = GridField()
        self.assertEqual(len(gridfield.values), 0)
        self.assertEqual(gridfield.grid.bounds.tuple, (0, 0, 0, 0))


if __name__ == "__main__":
    unittest.main()
