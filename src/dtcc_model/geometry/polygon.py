from dataclasses import dataclass, field
from .bounds import Bounds
from .geometry import Geometry
from shapely.geometry import Polygon as ShapelyPolygon


@dataclass
class Polygon(Geometry):
    geom: ShapelyPolygon = field(default_factory=ShapelyPolygon)

    def to_proto(self):
        return None

    def from_proto(self, pb):
        return None
