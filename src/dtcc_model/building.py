# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

import numpy as np
from shapely.geometry import Polygon
from typing import Any, Union
from dataclasses import dataclass, field

from .model import DTCCModel
from . import dtcc_pb2 as proto
from .pointcloud import PointCloud
from .utils import pb_polygon_to_shapely, pb_polygon_from_shapely


@dataclass
class Building(DTCCModel):
    """A base representation of a singele building.

    Attributes:
    uuid (str): The UUID of the building.
    footprint (Polygon): The polygon representing the footprint of the building.
    height (float): The height of the building.
    ground_level (float): The ground level of base of the building.
    roofpoints (PointCloud): The point cloud representing the roof points of the building.
    crs (str): The coordinate reference system of the building.
    error (int): Encoding the errors the occured when generating 3D represention of building.
    properties (dict): Additional properties of the building.

    """

    uuid: str = "NONE"
    footprint: Polygon = Polygon()
    height: float = 0
    ground_level: float = 0
    roofpoints: PointCloud = field(default_factory=PointCloud)
    crs: str = ""
    error: int = 0
    properties: dict = field(default_factory=dict)

    def __str__(self):
        return f"DTCC Building {self.uuid} with {self.footprint.area} m² footprint"

    @property
    def area(self):
        return self.footprint.area

    def from_proto(self, pb: Union[proto.Building, bytes]):
        if isinstance(pb, bytes):
            pb = proto.Building.FromString(pb)
        self.footprint = pb_polygon_to_shapely(pb.footprint)
        self.uuid = pb.uuid
        self.height = pb.height
        self.ground_level = pb.groundHeight
        self.error = pb.error
        self.roofpoints = PointCloud()
        self.roofpoints.points = np.array(pb.roofpoints.points).reshape(-1, 3)

    def to_proto(self) -> proto.Building:
        pb = proto.Building()
        pb.uuid = self.uuid
        pb.height = self.height
        pb.groundHeight = self.ground_level
        pb.error = self.error
        pb.footprint.CopyFrom(pb_polygon_from_shapely(self.footprint))
        pb.roofpoints.points.extend(self.roofpoints.points.flatten())
        return pb

    def __getitem__(self, key: str) -> Any:
        # handle special properties
        if key == "height":
            return self.height
        elif key == "ground_level":
            return self.ground_level
        elif key == "uuid":
            return self.uuid
        elif key == "error":
            return self.error
        # handle generic properties
        elif key in self.properties:
            return self.properties[key]
        else:
            raise KeyError(f"Property {key} not found")

    def __setitem__(self, key: str, value: Any):
        # handle special properties
        if key == "height":
            self.height = value
        elif key == "ground_level":
            self.ground_level = value
        elif key == "uuid":
            self.uuid = value
        elif key == "error":
            self.error = value
        # handle generic properties
        else:
            self.properties[key] = value
