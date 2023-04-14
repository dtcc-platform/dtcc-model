from dataclasses import dataclass
import numpy as np
from shapely.geometry import Polygon


@dataclass
class Building:
    uuid: str
    footprint: Polygon
    height: float
    ground_level: float
    roofpoints: np.ndarray  # or Pointcloud?
    crs: str
    error: int
    attributes: dict

    def __str__(self):
        return f"Building {self.uuid}"

    def area(self):
        return self.footprint.area
