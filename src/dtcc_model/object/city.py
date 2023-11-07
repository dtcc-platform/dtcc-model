# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

from dataclasses import dataclass

from .object import Object
from .building import NewBuilding as Building
from dtcc_model import dtcc_pb2 as proto


@dataclass
class NewCity(Object):
    """Represents a city, the top-level container class for city models."""

    def to_proto(self):
        return None

    def from_proto(self, pb):
        return None

    def add_buildings(self, buildings: list[Building]):
        for b in buildings:
            b.parents.append(self.id)
        self.children[Building] += buildings
