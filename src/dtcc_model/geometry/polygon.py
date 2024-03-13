from dataclasses import dataclass, field
from .bounds import Bounds
from .geometry import Geometry
from shapely.geometry import Polygon as ShapelyPolygon
import numpy as np


@dataclass
class Polygon(Geometry):
    geom: ShapelyPolygon = field(default_factory=ShapelyPolygon)

    def to_proto(self):
        return None

    def from_proto(self, pb):
        return None

    @property
    def shapely(self):
        return self.geom

    @property
    def vertices(self):
        return np.array(self.geom.exterior.coords)

    @property
    def holes(self):
        return [np.array(hole.coords) for hole in self.geom.interiors]

    @property
    def area(self):
        return self.geom.area
