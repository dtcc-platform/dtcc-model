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
    """A polygon representing a single landuse area.

    This class represents a polygon that defines a landuse area. Various landuse
    types are available, including: WATER, GRASS, FOREST, FARMLAND, URBAN,
    INDUSTRIAL, MILITARY, ROAD, and RAIL.

    Attributes
    ----------
    footprint : Polygon
        The geometric footprint of the landuse area represented as a Polygon.
    landuse : LanduseClasses
        The type of landuse associated with the area.
    properties : dict
        Additional properties or metadata associated with the landuse area.

    """

    footprint: Polygon = field(default_factory=Polygon)
    landuse: LanduseClasses = LanduseClasses.URBAN
    properties: dict = field(default_factory=dict)

    def __str__(self) -> str:
        """Return a string representation of the DTCC Landuse area.

        Returns
        -------
        str
            A string describing the Landuse object.

        """
        return f"DTCC Landuse area, type {self.landuse.name} with {self.footprint.area} m² footprint"

    @property
    def area(self) -> float:
        """Calculate the area of the landuse footprint.

        Returns
        -------
        float
            The area of the landuse area in square meters.

        """
        return self.footprint.area

    def to_proto(self) -> proto.LandUse:
        """Convert the Landuse object to a Protocol Buffers message.

        Returns
        -------
        proto.LandUse
            A Protocol Buffers message representing the Landuse object.

        """
        pb = proto.LandUse()
        pb.footprint.CopyFrom(pb_polygon_from_shapely(self.footprint))
        pb.type = self.landuse.name

        return pb

    def from_proto(self, pb: Union[proto.LandUse, bytes]):
        """Initialize the Landuse object from a Protocol Buffers message.

        This method populates the Landuse object's attributes based on the
        information in a Protocol Buffers message.

        Parameters
        ----------
        pb : Union[proto.LandUse, bytes]
            The Protocol Buffers message or its serialized bytes representation.

        """
        if isinstance(pb, bytes):
            pb = proto.Landuse.FromString(pb)
        self.footprint = pb_polygon_to_shapely(pb.footprint)
        self.landuse = LanduseClasses[pb.type.upper()]
