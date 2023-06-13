from typing import Any, Union, List
from dataclasses import dataclass, field
from shapely.geometry import LineString
import numpy as np
from enum import Enum, auto

from . import dtcc_pb2 as proto
from .model import DTCCModel
from .geometry import Georef


class RoadType(Enum):
    MOTORWAY = auto()

    PRIMARY = auto()
    SECONDARY = auto()
    TERTIARY = auto()
    RESIDENTIAL = auto()
    SERVICE = auto()
    TRACK = auto()
    PEDESTRIAN = auto()
    CYCLEWAY = auto()
    FOOTWAY = auto()
    BRIDLEWAY = auto()
    PATH = auto()


@dataclass
class Road(DTCCModel):
    road_geometry: LineString = field(default_factory=LineString)
    road_vertices: List[int] = field(default_factory=list)
    road_type: RoadType = RoadType.PRIMARY
    road_width: float = 0
    tunnel: bool = False
    bridge: bool = False
    lanes: int = 1
    speed_limit: float = 0
    road_name: str = ""
    road_id: str = ""

    def __str__(self):
        return f"DTCC Road {self.road_id} with {self.road_geometry.length} m length"

    @property
    def length(self):
        return self.road_geometry.length

    def to_proto(self) -> proto.Road:
        pb = proto.Road()
        pb.vertices.extend(self.road_vertices)
        pb.type = self.road_type
        pb.width = self.road_width
        pb.lanes = self.lanes
        pb.speedLimit = self.speed_limit
        pb.name = self.road_name
        pb.id = self.road_id
        return pb

    def from_proto(self, pb: Union[proto.Road, bytes]):
        if isinstance(pb, bytes):
            pb = proto.Road.FromString(pb)
        self.road_vertices = pb.vertices
        self.road_type = pb.type
        self.road_width = pb.width
        self.lanes = pb.lanes
        self.speed_limit = pb.speedLimit
        self.road_name = pb.name
        self.road_id = pb.id


@dataclass
class RoadNetwork(DTCCModel):
    roads: list[Road] = field(default_factory=list)
    vertices: np.ndarray = field(default_factory=lambda: np.empty(0))
    georef: Georef = field(default_factory=Georef)

    def __str__(self):
        return f"DTCC RoadNetwork with {len(self.roads)} roads"

    def to_proto(self) -> proto.RoadNetwork:
        pb = proto.RoadNetwork()
        pb.vertices.extend(self.vertices.flatten())
        pb.roads.extend([r.to_proto() for r in self.roads])

        return pb

    def from_proto(self, pb: Union[proto.RoadNetwork, bytes]):
        if isinstance(pb, bytes):
            pb = proto.RoadNetwork.FromString(pb)
        self.vertices = np.array(pb.vertices).reshape(-1, 2)
        self.roads = [Road().from_proto(r) for r in pb.roads]
        for i, r in enumerate(self.roads):
            r.road_geometry = LineString(self.vertices[r.road_vertices])
            self.roads[i] = r
