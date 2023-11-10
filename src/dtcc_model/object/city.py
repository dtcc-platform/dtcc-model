# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

from dataclasses import dataclass

from .object import Object
from .building import NewBuilding as Building
from dtcc_model import dtcc_pb2 as proto


@dataclass
class NewCity(Object):
    """Represents a city, the top-level container class for city models."""

    @property
    def buildings(self):
        """Return list of buildings in city."""
        return self.children[Building] if Building in self.children else []

    @property
    def num_buildings(self):
        """Return number of buildings in city."""
        return len(self.buildings)
