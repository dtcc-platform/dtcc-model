# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

from dataclasses import dataclass

from .object import Object
from dtcc_model import dtcc_pb2 as proto


@dataclass
class Building(Object):
    """Represents a building in a city."""

    # TODO: Implement to_proto and from_proto
    def to_proto(self):
        pass

    def from_proto(self, pb):
        pass


class BuildingPart(Object):
    # TODO: Implement to_proto and from_proto
    def to_proto(self):
        pass

    def from_proto(self, pb):
        pass
