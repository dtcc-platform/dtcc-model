from typing import Any, Union, List
from dataclasses import dataclass, field
from shapely.geometry import LineString
import numpy as np
from enum import Enum, auto

from . import dtcc_pb2 as proto
from .model import DTCCModel
from .geometry import Georef


class RoadType(Enum):
    """Enumeration representing different road types."""
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

    """
    A representation of a road.

    This class represents a road with various attributes, including geometry, road type, width,
    tunnel/bridge information, number of lanes, speed limit, road name, and road ID.

    Attributes
    ----------
    road_geometry : shapely.geometry.LineString
        The geometry of the road as a LineString.
    road_vertices : List[int]
        The vertices representing the road geometry.
    road_type : RoadType
        The type of road (e.g., PRIMARY, SECONDARY).
    road_width : float
        The width of the road.
    tunnel : bool
        Indicates whether the road is a tunnel.
    bridge : bool
        Indicates whether the road is a bridge.
    lanes : int
        The number of lanes on the road.
    speed_limit : float
        The speed limit on the road.
    road_name : str
        The name of the road.
    road_id : str
        The unique identifier of the road.

    """

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
        """
        Return a string representation of the Road, containing its road ID and length.

        Returns
        -------
        str
            A string representation of the Road.

        """
        return f"DTCC Road {self.road_id} with {self.road_geometry.length} m length"

    @property
    def length(self):
        """
        Get the length of the road geometry.

        Returns
        -------
        float
            The length of the road geometry in meters.

        """
        return self.road_geometry.length

    def to_proto(self) -> proto.Road:
        """
        Convert the Road object to a protobuf representation.

        Returns
        -------
        proto.Road
            A protobuf representation of the Road.

        """
        pb = proto.Road()
        pb.vertices.extend(self.road_vertices)
        pb.type = self.road_type
        pb.width = self.road_width
        pb.lanes = self.lanes
        pb.speed_limit = self.speed_limit
        pb.name = self.road_name
        pb.id = self.road_id
        return pb

    def from_proto(self, pb: Union[proto.Road, bytes]):
        """
        Initialize the Road object from a protobuf representation.

        Parameters
        ----------
        pb : Union[proto.Road, bytes]
            A protobuf representation of the Road or a bytes object.

        Returns
        -------
        None
        """
        if isinstance(pb, bytes):
            pb = proto.Road.FromString(pb)
        self.road_vertices = pb.vertices
        self.road_type = pb.type
        self.road_width = pb.width
        self.lanes = pb.lanes
        self.speed_limit = pb.speed_limit
        self.road_name = pb.name
        self.road_id = pb.id


@dataclass
class RoadNetwork(DTCCModel):
    """
    A representation of a road network.

    This class represents a road network consisting of multiple roads, vertices, and georeference
    information.

    Attributes
    ----------
    roads : List[Road]
        A list of Road objects representing the roads in the network.
    vertices : np.ndarray
        An array of vertices representing the network topology.
    georef : Georef
        The georeference information for the network.

    """

    roads: List[Road] = field(default_factory=list)
    vertices: np.ndarray = field(default_factory=lambda: np.empty(0))
    georef: Georef = field(default_factory=Georef)

    def __str__(self):
        """
        Return a string representation of the RoadNetwork.

        Returns
        -------
        str
            A string representation of the RoadNetwork.

        """
        return f"DTCC RoadNetwork with {len(self.roads)} roads"

    def to_proto(self) -> proto.RoadNetwork:
        """
        Convert the RoadNetwork object to a protobuf representation.

        Returns
        -------
        proto.RoadNetwork
            A protobuf representation of the RoadNetwork.

        """
        pb = proto.RoadNetwork()
        pb.vertices.extend(self.vertices.flatten())
        pb.roads.extend([r.to_proto() for r in self.roads])

        return pb

    def from_proto(self, pb: Union[proto.RoadNetwork, bytes]):
        """
        Initialize the RoadNetwork object from a protobuf representation.

        Parameters
        ----------
        pb : Union[proto.RoadNetwork, bytes]
            A protobuf representation of the RoadNetwork or a bytes object.

        Returns
        -------
        None

        """
        if isinstance(pb, bytes):
            pb = proto.RoadNetwork.FromString(pb)
        self.vertices = np.array(pb.vertices).reshape(-1, 2)
        self.roads = [Road().from_proto(r) for r in pb.roads]
        for i, r in enumerate(self.roads):
            r.road_geometry = LineString(self.vertices[r.road_vertices])
            self.roads[i] = r
