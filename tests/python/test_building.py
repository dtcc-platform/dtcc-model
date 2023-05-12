import unittest
from pathlib import Path
from dtcc_model.building import Building

data_dir = (Path(__file__).parent / ".." / "data").resolve()


class TestBuilding(unittest.TestCase):
    def test_empty(self):
        b = Building()
        self.assertEqual(b.uuid, "NONE")
        self.assertEqual(b.footprint.area, 0)
        self.assertEqual(b.height, 0)
        self.assertEqual(b.ground_level, 0)
        self.assertEqual(len(b.roofpoints), 0)
        self.assertEqual(b.crs, "")
        self.assertEqual(b.error, 0)
        self.assertEqual(b.properties, {})

    def test_from_proto(self):
        b = Building()
        with (data_dir / "building1.pb").open("rb") as f:
            b.from_proto(f.read())
        self.assertEqual(b.uuid, "0-1")
        self.assertGreater(b.area, 10)

    def test_to_proto(self):
        b = Building()
        with (data_dir / "building2.pb").open("rb") as f:
            b.from_proto(f.read())
        # tmpfile = NamedTemporaryFile(suffix=".pb", delete=False)
        pb_building = b.to_proto()
        self.assertEqual(pb_building.uuid, "3")
        self.assertEqual(len(pb_building.footPrint.shell.vertices), 5)
        self.assertEqual(len(pb_building.footPrint.holes), 1)

    def test_getitem(self):
        b = Building()
        with (data_dir / "building2.pb").open("rb") as f:
            b.from_proto(f.read())
        self.assertEqual(b["uuid"], "3")
        self.assertEqual(b["height"], 0)
        self.assertEqual(b["ground_level"], 0)
        self.assertEqual(b["error"], 0)
        with self.assertRaises(KeyError):
            b["foo"]

        # self.assertRaises(b["foo"], KeyError)
        b["foo"] = "bar"
        self.assertEqual(b["foo"], "bar")
