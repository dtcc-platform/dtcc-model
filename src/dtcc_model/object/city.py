# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

from dataclasses import dataclass
from typing import Union

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

    def to_proto(self) -> proto.Object:
        """Return a protobuf representation of the City.

        Returns
        -------
        proto.Object
            A protobuf representation of the City as an Object.
        """

        # Handle Object fields
        pb = Object.to_proto(self)

        # Handle specific fields (currently none)
        _pb = proto.City()
        pb.city.CopyFrom(_pb)

        return pb

    def from_proto(self, pb: Union[proto.Object, bytes]):
        """Initialize City from a protobuf representation.

        Parameters
        ----------
        pb: Union[proto.Object, bytes]
            The protobuf message or its serialized bytes representation.
        """

        # Handle byte representation
        if isinstance(pb, bytes):
            pb = proto.Object.FromString(pb)

        # Handle Object fields
        Object.from_proto(self, pb)

        # Handle specific fields (currently none)
        pass


@dataclass
class CityObject(Object):
    """Represents a generic object in a city."""

    def to_proto(self) -> proto.Object:
        """Return a protobuf representation of the CityObject.

        Returns
        -------
        proto.Object
            A protobuf representation of the CityObject as an Object.
        """

        # Handle Object fields
        pb = Object.to_proto(self)

        # Handle specific fields (currently none)
        _pb = proto.CityObject()
        pb.city.CopyFrom(_pb)

        return pb

    def from_proto(self, pb: Union[proto.Object, bytes]):
        """Initialize CityObject from a protobuf representation.

        Parameters
        ----------
        pb: Union[proto.Object, bytes]
            The protobuf message or its serialized bytes representation.
        """

        # Handle byte representation
        if isinstance(pb, bytes):
            pb = proto.Object.FromString(pb)

        # Handle Object fields
        Object.from_proto(self, pb)

        # Handle specific fields (currently none)
        pass
