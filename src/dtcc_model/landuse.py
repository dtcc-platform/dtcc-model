# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

from shapely.geometry import Polygon
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Union

from .utils import pb_polygon_to_shapely, pb_polygon_from_shapely

from .model import DTCCModel
from . import dtcc_pb2 as proto


class LanduseClasses(Enum):
    WATER = auto()
    GRASS = auto()
    FOREST = auto()
    FARMLAND = auto()
    URBAN = auto()
    INDUSTRIAL = auto()
    MILITARY = auto()
    ROAD = auto()
    RAIL = auto()


@dataclass
class Landuse(DTCCModel):
    footprint: Polygon = field(default_factory=Polygon)
    landuse: LanduseClasses = LanduseClasses.URBAN
    properties: dict = field(default_factory=dict)

    def __str__(self) -> str:
        return f"DTCC Landuse area, type {self.landuse.name} with {self.footprint.area} m² footprint"

    @property
    def area(self) -> float:
        return self.footprint.area

    def to_proto(self) -> proto.LandUse:
        pb = proto.LandUse()
        pb.footprint.CopyFrom(pb_polygon_from_shapely(self.footprint))
        pb.type = self.landuse.name

        return pb

    def from_proto(self, pb: Union[proto.LandUse, bytes]):
        if isinstance(pb, bytes):
            pb = proto.Landuse.FromString(pb)
        self.footprint = pb_polygon_to_shapely(pb.footprint)
        self.landuse = LanduseClasses[pb.type.upper()]
