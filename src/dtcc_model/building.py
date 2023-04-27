# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

import numpy as np
from shapely.geometry import Polygon
from typing import Union
from dataclasses import dataclass, field
from inspect import getmembers, isfunction, ismethod

from .model import DTCCModel
from . import dtcc_pb2 as proto
from .pointcloud import PointCloud
from .utils import pb_polygon_to_shapely, pb_polygon_from_shapely


@dataclass
class Building(DTCCModel):
    uuid: str = "NONE"
    footprint: Polygon = Polygon()
    height: float = 0
    ground_level: float = 0
    roofpoints: PointCloud = field(default_factory=PointCloud)
    crs: str = ""
    error: int = 0
    attributes: dict = field(default_factory=dict)

    def __str__(self):
        return f"DTCC Building {self.uuid} with {self.footprint.area} m² footprint"

    def area(self):
        return self.footprint.area

    def from_proto(self, pb: Union[proto.Building, bytes]):
        if isinstance(pb, bytes):
            pb = proto.Building.FromString(pb)
        self.footprint = pb_polygon_to_shapely(pb.footPrint)
        self.uuid = pb.uuid
        self.height = pb.height
        self.ground_level = pb.groundHeight
        self.error = pb.error
        self.roofpoints = np.array([[v.x, v.y, v.z] for v in pb.roofpoints.points])

    def to_proto(self) -> proto.Building:
        pb = proto.Building()
        pb.uuid = self.uuid
        pb.height = self.height
        pb.groundHeight = self.ground_level
        pb.error = self.error
        pb.footPrint.CopyFrom(pb_polygon_from_shapely(self.footprint))
        pb.roofpoints.points.extend(
            [proto.Vector3D(x=p[0], y=p[1], z=p[2]) for p in self.roofpoints]
        )
        return pb

    @classmethod
    def add_processors(cls, module):
        for fn_name, fn in getmembers(module, isfunction):
            print(fn_name)
            if not fn_name.startswith("_"):
                setattr(cls, fn_name, fn)

    @classmethod
    def show_processors(cls, verbose=False):
        print(f"Processors for {cls.__name__}:")
        for fn_name, fn in getmembers(cls, isfunction):
            if not fn_name.startswith("_"):
                print(f" - {fn_name}: from {fn.__module__}.{fn.__qualname__}")
                if verbose:
                    print(f"   {fn.__doc__}")
