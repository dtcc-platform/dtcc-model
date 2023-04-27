# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

import numpy as np
from typing import Union, List
from dataclasses import dataclass, field
from inspect import getmembers, isfunction, ismethod

from .model import DTCCModel
from . import dtcc_pb2 as proto
from .geometry import Bounds, Georef
from .raster import Raster
from .gridfields import GridField
from .building import Building


@dataclass
class CityModel(DTCCModel):
    bounds: Bounds = field(default_factory=Bounds)
    georef: Georef = field(default_factory=Georef)
    terrain: Raster = field(default_factory=Raster)
    buildings: List[Building] = field(default_factory=list)
    bounds: Bounds = field(default_factory=Bounds)

    def __str__(self):
        return f"DTCC CityModel on {self.bounds.bndstr} with {len(self.buildings)} building(s)"

    @property
    def origin(self):
        return (self.bounds.xmin, self.bounds.ymin)

    def add_building(self, building: Building):
        self.buildings.append(building)

    def from_proto(self, pb: Union[proto.CityModel, bytes]):
        if isinstance(pb, bytes):
            pb = proto.CityModel.FromString(pb)
        self.bounds.from_proto(pb.bounds)
        self.georef.from_proto(pb.georefer)
        self.terrain.from_proto(pb.terrain)
        self.buildings = [Building.from_proto(b) for b in pb.buildings]

    def to_proto(self) -> proto.CityModel:
        pb = proto.CityModel()
        pb.bounds.CopyFrom(self.bounds.to_proto())
        pb.georef.CopyFrom(self.georef.to_proto())
        pb.terrain.CopyFrom(self.terrain.to_proto())
        pb.buildings.extend(self.buildings)
        return pb
