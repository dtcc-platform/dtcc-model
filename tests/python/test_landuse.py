import unittest
from pathlib import Path
from dtcc_model.landuse import Landuse

data_dir = (Path(__file__).parent / ".." / "data").resolve()


class TestLanduse(unittest.TestCase):
    def test_empty(self):
        lu = Landuse()
        self.assertEqual(lu.landuse.name, "URBAN")
        self.assertEqual(lu.area, 0)
        self.assertEqual(lu.properties, {})

    def test_protobuf(self):
        lu = Landuse()
        pb = lu.to_proto()
        self.assertEqual(pb.type, "URBAN")
        lu2 = Landuse()
        lu2.from_proto(pb)
        self.assertEqual(lu2.landuse.name, "URBAN")
