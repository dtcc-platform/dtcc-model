# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

from dataclasses import dataclass, field

from .object import Object
from dtcc_model.geometry import Bounds
from dtcc_model.object import GeometryType
from shapely.geometry import Polygon


@dataclass
class Building(Object):
    """Represents a building in a city."""

    @property
    def building_parts(self):
        """Return list of building parts in building."""
        return self.children[BuildingPart] if BuildingPart in self.children else []

    @property
    def height(self):
        self.bounds.zmax

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
