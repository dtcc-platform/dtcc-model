# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

from dataclasses import dataclass

from .object import Object
from .building import Building
from .terrain import Terrain

from dtcc_model import dtcc_pb2 as proto


@dataclass
class City(Object):
    """Represents a city, the top-level container class for city models."""

    @property
    def buildings(self):
        """Return list of buildings in city."""
        return self.children[Building] if Building in self.children else []

    @property
    def terrain(self):
        """Return terrain in city."""
        if Terrain in self.children:
            return self.children[Terrain][0]
        else:
            return Terrain()

    @property
    def num_buildings(self):
        """Return number of buildings in city."""
        return len(self.buildings)

    def add_terrain(self, terrain):
        """Add terrain to city."""
        self.add_child(terrain)

    def add_buildings(self, buildings: list[Building]):
        """Add building to city."""
        self.add_children(buildings)

    def to_proto(self):
        """Return a protobuf representation of the City.

        Returns
        -------
        proto.City
            A protobuf representation of the Building and as an Object.
        """

        # Handle Object fields
        pb = Object.to_proto(self)

        # Handle specific fields (currently none)
        _city = proto.City()
        pb.city.CopyFrom(_city)

        return pb

    def from_proto(self, pb):
        """Initialize City from a protobuf representation.

        Parameters
        ----------
        pb: Union[proto.Object, bytes]
            The protobuf message or its serialized bytes representation.
        """

        # Handle Object fields
        Object.from_proto(self, pb)

        # Handle specific fields (currently none)
        pass


@dataclass
class CityObject(Object):
    """Fallback for any object in a City which doesn't have a more specific object class."""

    def to_proto(self):
        pass

    def from_proto(self, pb):
        pass
