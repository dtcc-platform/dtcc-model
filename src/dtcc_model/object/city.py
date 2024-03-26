# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

from dataclasses import dataclass

from .object import Object, GeometryType
from .raster import Raster
from .building import Building
from .terrain import Terrain
from dtcc_model import geometry

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
        if isinstance(terrain, Terrain):
            self.add_child(terrain)
        else:
            terrain_object = Terrain()
            if isinstance(terrain, Raster):
                terrain_object.add_geometry(terrain, GeometryType.RASTER)
            elif isinstance(terrain, geometry.Mesh):
                terrain_object.add_geometry(terrain, GeometryType.MESH)
            else:
                raise ValueError(f"Invalid terrain type {type(terrain)}.")
            self.add_child(terrain_object)

    def add_buildings(self, buildings: list[Building]):
        """Add building to city."""
        self.add_children(buildings)

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
