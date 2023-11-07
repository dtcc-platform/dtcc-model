# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

from dataclasses import dataclass, field

from .object import Object
from dtcc_model import dtcc_pb2 as proto


@dataclass
class NewBuilding(Object):
    """Represents a building in a city."""

    pass

    def to_proto(self):
        return None

    def from_proto(self, pb):
        return None
