import unittest
from pathlib import Path

from dtcc_model.roadnetwork import Road, RoadNetwork, RoadType


class TestRoadNetwork(unittest.TestCase):
    def test_empty_roadnetwork(self):
        rn = RoadNetwork()
        self.assertEqual(len(rn.roads), 0)
        self.assertEqual(rn.georef.crs, "")

    def test_empty_road(self):
        road = Road()
        self.assertEqual(road.road_id, "")
        self.assertEqual(road.road_name, "")
        self.assertEqual(road.road_type, RoadType.PRIMARY)
        self.assertEqual(road.road_width, 0)
        self.assertEqual(road.lanes, 1)
        self.assertEqual(road.speed_limit, 0)
        self.assertEqual(road.length, 0)


if __name__ == "__main__":
    unittest.main()
