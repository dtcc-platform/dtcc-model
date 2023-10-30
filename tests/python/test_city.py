import unittest
from pathlib import Path
from dtcc_model.building import Building
from dtcc_model.city import City
from tempfile import NamedTemporaryFile
import json

data_dir = (Path(__file__).parent / ".." / "data").resolve()


class TestCity(unittest.TestCase):
    def test_empty(self):
        city = City()
        self.assertEqual(len(city.buildings), 0)
        self.assertEqual(city.georef.crs, "")
        self.assertEqual(city.bounds.tuple, (0, 0, 0, 0))

    def test_protobuf_roundtrip(self):
        city = City()
        city.name = "test123"
        self.assertEqual(city.name, "test123")
        pb_city = city.to_proto()
        pb_filename = NamedTemporaryFile(suffix=".pb", delete=True)
        with open(pb_filename.name, "wb") as f:
            f.write(pb_city.SerializeToString())
        city2 = City()
        with open(pb_filename.name, "rb") as f:
            city2.from_proto(f.read())
        self.assertEqual(city2.name, "test123")
        pb_filename.close()

    def test_to_json(self):
        city = City()
        city.name = "test123"
        self.assertEqual(city.name, "test123")
        json_city_str = city.to_json()
        self.assertTrue(isinstance(json_city_str, str))
        json_city = json.loads(json_city_str)
        self.assertEqual(json_city["name"], "test123")

    # def test_from_proto(self):
    #     city = City()
    #     with (data_dir / "City.pb").open("rb") as f:
    #         city.from_proto(f.read())
    #     self.assertEqual(len(city.buildings), 5)

    #     self.assertEqual(city.buildings[0].uuid, "0-0")
    #     self.assertEqual(city.buildings[1].uuid, "0-1")
    #     self.assertEqual(city.crs, "EPSG:3857")
    #     self.assertEqual(city.origin, (0, 0))
    #     self.assertEqual(city.bounds, (0, 0, 0, 0))

    # def test_to_proto(self):
    #     city = City()
    #     with (data_dir / "City.pb").open("rb") as f:
    #         city.from_proto(f.read())
    #     # tmpfile = NamedTemporaryFile(suffix=".pb", delete=False)
    #     pb_city = city.to_proto()
    #     self.assertEqual(len(pb_city.buildings), 5)
    #     self.assertEqual(pb_city.georeference.crs, "EPSG:3857")
    #     self.assertEqual(pb_city.georeference.x0, 0)
    #     self.assertEqual(pb_city.georeference.y0, 0)
    #     self.assertEqual(pb_city.bounds.p.x, 0)
    #     self.assertEqual(pb_city.bounds.p.y, 0)
    #     self.assertEqual(pb_city.bounds.q.x, 0)
    #     self.assertEqual(pb_city.bounds.q.y, 0)


if __name__ == "__main__":
    unittest.main()
