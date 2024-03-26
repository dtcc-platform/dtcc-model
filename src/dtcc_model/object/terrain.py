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

    def __str__(self):
        out_str = "Terrain object"
        if self.mesh is not None:
            out_str += f" with mesh {self.mesh}"
        if self.raster is not None:
            out_str += f" with raster {self.raster}"
        return out_str
