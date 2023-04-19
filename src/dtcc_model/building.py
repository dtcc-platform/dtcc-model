# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

import numpy as np
from shapely.geometry import Polygon
from typing import Union
from dataclasses import dataclass, field

from . import dtcc_pb2 as proto
from .utils import pb_polygon_to_shapely, pb_polygon_from_shapely


@dataclass
class Building:
    uuid: str = 'NONE'
    footprint: Polygon = Polygon()
    height: float = 0
    ground_level: float = 0
    roofpoints: np.ndarray = np.empty(
        (0, 3), dtype=np.float64)  # or Pointcloud?
    crs: str = ''
    error: int = 0
    attributes: dict = field(default_factory=dict)

    def __str__(self):
        return f'DTCC Building {self.uuid} with {self.footprint.area} m² footprint'

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
        self.roofpoints = np.array(
            [[v.x, v.y, v.z] for v in proto_building.roofpoints.points]
        )

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
