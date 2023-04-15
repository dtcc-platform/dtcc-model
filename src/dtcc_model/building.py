from dataclasses import dataclass, field
import numpy as np
from shapely.geometry import Polygon
from typing import Union
import dtcc_model.dtcc_pb2 as proto
from .utils import pb_polygon_to_shapely, pb_polygon_from_shapely


@dataclass
class Building:
    uuid: str = ""
    footprint: Polygon = Polygon()
    height: float = 0
    ground_level: float = 0
    roofpoints: np.ndarray = np.empty((0, 3), dtype=np.float64)  # or Pointcloud?
    crs: str = ""
    error: int = 0
    attributes: dict = field(default_factory=dict)

    def __str__(self):
        return f"Building {self.uuid} with {self.footprint.area} m² footprint"

    def area(self):
        return self.footprint.area

    def from_proto(self, proto_building: Union[proto.Building, bytes]):
        if isinstance(proto_building, bytes):
            _building = proto.Building()
            _building.ParseFromString(proto_building)
            proto_building = _building
        self.footprint = pb_polygon_to_shapely(proto_building.footPrint)
        self.uuid = proto_building.uuid
        self.height = proto_building.height
        self.ground_level = proto_building.groundHeight
        self.error = proto_building.error
        self.roofpoints = np.array(
            [[v.x, v.y, v.z] for v in proto_building.roofpoints.points]
        )

    def to_proto(self) -> proto.Building:
        _building = proto.Building()
        _building.uuid = self.uuid
        _building.height = self.height
        _building.groundHeight = self.ground_level
        _building.error = self.error
        _building.footPrint.CopyFrom(pb_polygon_from_shapely(self.footprint))
        _building.roofpoints.points.extend(
            [proto.Vector3D(x=p[0], y=p[1], z=p[2]) for p in self.roofpoints]
        )
        return _building
