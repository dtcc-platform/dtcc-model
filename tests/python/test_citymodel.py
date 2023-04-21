import unittest
from pathlib import Path
from dtcc_model.building import Building
from dtcc_model.citymodel import CityModel

data_dir = (Path(__file__).parent / ".." / "data").resolve()


class TestCityModel(unittest.TestCase):
    def test_empty(self):
        cm = CityModel()
        self.assertEqual(len(cm.buildings), 0)
        self.assertEqual(cm.georef.crs, "")
        self.assertEqual(cm.bounds.tuple, (0, 0, 0, 0))

    # def test_from_proto(self):
    #     cm = CityModel()
    #     with (data_dir / "CityModel.pb").open("rb") as f:
    #         cm.from_proto(f.read())
    #     self.assertEqual(len(cm.buildings), 5)

    #     self.assertEqual(cm.buildings[0].uuid, "0-0")
    #     self.assertEqual(cm.buildings[1].uuid, "0-1")
    #     self.assertEqual(cm.crs, "EPSG:3857")
    #     self.assertEqual(cm.origin, (0, 0))
    #     self.assertEqual(cm.bounds, (0, 0, 0, 0))

    # def test_to_proto(self):
    #     cm = CityModel()
    #     with (data_dir / "CityModel.pb").open("rb") as f:
    #         cm.from_proto(f.read())
    #     # tmpfile = NamedTemporaryFile(suffix=".pb", delete=False)
    #     pb_citymodel = cm.to_proto()
    #     self.assertEqual(len(pb_citymodel.buildings), 5)
    #     self.assertEqual(pb_citymodel.georeference.crs, "EPSG:3857")
    #     self.assertEqual(pb_citymodel.georeference.x0, 0)
    #     self.assertEqual(pb_citymodel.georeference.y0, 0)
    #     self.assertEqual(pb_citymodel.bounds.p.x, 0)
    #     self.assertEqual(pb_citymodel.bounds.p.y, 0)
    #     self.assertEqual(pb_citymodel.bounds.q.x, 0)
    #     self.assertEqual(pb_citymodel.bounds.q.y, 0)
