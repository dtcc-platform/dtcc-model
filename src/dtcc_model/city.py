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

from .building import Building
from .landuse import Landuse
from .roadnetwork import RoadNetwork


@dataclass
class City(DTCCModel):
    """A City is the top-level container class for city models.

    This class represents a city model and serves as a container for various
    city-related data, including terrain, buildings, land use, and road networks.

    Attributes
    ----------
    name : str
        The name of the city.
    bounds : Bounds
        The geographic boundaries of the city.
    georef : Georef
        The georeferencing information for the city.
    terrain : Raster
        The raster data representing the terrain of the city.
    buildings : List[Building]
        A list of building objects in the city.
    landuse : List[Landuse]
        A list of land use objects in the city.
    roadnetwork : RoadNetwork
        The road network data for the city.

    """

    name: str = ""
    bounds: Bounds = field(default_factory=Bounds)
    georef: Georef = field(default_factory=Georef)
    terrain: Raster = field(default_factory=Raster)
    buildings: List[Building] = field(default_factory=list)
    landuse: List[Landuse] = field(default_factory=list)
    roadnetwork: RoadNetwork = field(default_factory=RoadNetwork)

    def __str__(self):
        """Provide a human-readable representation of the City.

        Returns
        -------
        str
            A string representation of the city with its boundaries and number of buildings.

        """
        return (
            f"DTCC City on {self.bounds.bndstr} with {len(self.buildings)} building(s)"
        )

    @property
    def origin(self):
        """Get the origin coordinates of the city's bounding box.

        Returns
        -------
        Tuple[float, float]
            A tuple representing the (x, y) coordinates of the origin.
        """
        return (self.bounds.xmin, self.bounds.ymin)

    def add_building(self, building: Building):
        """Add a building to the city's list of buildings.

        Parameters
        ----------
        building : Building
            The building object to add to the city.
        """
        self.buildings.append(building)

    def from_proto(self, pb: Union[proto.City, bytes]):
        """Initialize the City object from a Protocol Buffers message.

        This method populates the City object's attributes based on the
        information in a Protocol Buffers message.

        Parameters
        ----------
        pb : Union[proto.City, bytes]
            The Protocol Buffers message or its serialized bytes representation.

        """
        if isinstance(pb, bytes):
            pb = proto.City.FromString(pb)
        self.name = pb.name
        self.bounds.from_proto(pb.bounds)
        self.georef.from_proto(pb.georef)
        self.terrain.from_proto(pb.terrain)

        self.buildings = []
        for b in pb.buildings:
            building = Building()
            building.from_proto(b)
            self.buildings.append(building)
        self.landuse = []
        for l in pb.landuse:
            landuse = Landuse()
            landuse.from_proto(l)
            self.landuse.append(landuse)

    def to_proto(self) -> proto.City:
        """Convert the City object to a Protocol Buffers message.

        Returns
        -------
        proto.City
            A Protocol Buffers message representing the City object.

        """
        pb = proto.City()
        pb.name = self.name
        pb.bounds.CopyFrom(self.bounds.to_proto())
        pb.georef.CopyFrom(self.georef.to_proto())
        pb.terrain.CopyFrom(self.terrain.to_proto())
        pb.buildings.extend([b.to_proto() for b in self.buildings])
        pb.landuse.extend([lu.to_proto() for lu in self.landuse])
        return pb
