# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

from dataclasses import dataclass

from .object import Object
from .building import Building
from dtcc_model import dtcc_pb2 as proto


@dataclass
class City(Object):
    """Represents a city, the top-level container class for city models."""

    @property
    def buildings(self):
        """Return list of buildings in city."""
        return self.children[Building] if Building in self.children else []

    @property
    def num_buildings(self):
        """Return number of buildings in city."""
        return len(self.buildings)

    # TODO: Implement to_proto and from_proto
    def to_proto(self):
        pass

    def from_proto(self, pb):
        pass


@dataclass
class CityObject(Object):
    """Fallback for any object in a City which doesn't have a more specific object class."""

    def to_proto(self):
        pass

    def from_proto(self, pb):
        pass
