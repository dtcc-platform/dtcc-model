# Copyright(C) 2024 Dag Wästberg
# Licensed under the MIT License

from dataclasses import dataclass

from .object import Object


@dataclass
class Terrain(Object):
    """Represents a terrain object in a city."""

    # TODO: Implement to_proto and from_proto
    def to_proto(self):
        pass

    def from_proto(self, pb):
        pass
