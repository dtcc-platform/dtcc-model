# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

from dataclasses import dataclass, field
from collections import defaultdict
from enum import Enum, auto

from dtcc_model.model import Model
from dtcc_model.geometry import Geometry


class GeometryType(Enum):
    BOUNDS = auto()
    LOD0 = auto()
    LOD1 = auto()
    LOD2 = auto()
    LOD3 = auto()
    MESH = auto()
    VOLUME_MESH = auto()
    POINT_CLOUD = auto()
    RASTER = auto()
    POLYGON = auto()
    LINESTRING = auto()

    @staticmethod
    def from_str(s):
        s = s.upper()
        try:
            t = GeometryType[s]
        except KeyError:
            raise ValueError(f"Unknown geometry type: {s}")
        return t


@dataclass
class Object(Model):
    """Base class for all object classes.

    Object classes represent city objects such as buildings, roads, and trees.
    Each object has a unique identifier (.id) and a set of attributes
    (.attributes). Objects may also have children and parents.

    The geometry of an object may have different representations, e.g., in
    different levels of detail (LOD). The geometries of an Object are stored in
    a dictionary, where the keys identify the type of representation, e.g.,
    "lod0", "lod1", etc.

    Attributes
    ----------
    id : str
        Unique identifier of the object.
    attributes : dict
        Dictionary of attributes.
    children : dict of lists
        Dictionary of child objects (key is type).
    parents : dict of lists
        Dictionary of parent objects (key is type).
    geometry : dict
        Dictionary of geometries.
    """

    id: str = ""
    attributes: dict = field(default_factory=dict)
    children: dict = field(default_factory=lambda: defaultdict(list))
    parents: dict = field(default_factory=lambda: defaultdict(list))
    geometry: dict = field(default_factory=dict)

    def flatten_geometry(self, geom_type: GeometryType):
        """Returns a single geometry of the specified type, merging all the geometries of the children."""
        geom = self.geometry.get(geom_type, None)

        for child_list in self.children.values():
            for child in child_list:
                child_geom = child.geometry.get(geom_type, None)
                if geom is None and child_geom is not None:
                    geom = child_geom
                if child_geom is not None:
                    geom.merge(child_geom)
        return geom

    @property
    def num_children(self):
        """Return number of child objects."""
        return len(self.children)

    @property
    def num_parents(self):
        """Return number of parent objects."""
        return len(self.parents)

    @property
    def bounds(self):
        """Return bounds of object."""
        return self.geometry.get(GeometryType.BOUNDS, None)

    @property
    def lod0(self):
        """Return LOD0 geometry."""
        return self.geometry.get(GeometryType.LOD0, None)

    @property
    def lod1(self):
        """Return LOD0 geometry."""
        return self.geometry.get(GeometryType.LOD1, None)

    @property
    def lod2(self):
        """Return LOD0 geometry."""
        return self.geometry.get(GeometryType.LOD2, None)

    @property
    def lod3(self):
        """Return LOD0 geometry."""
        return self.geometry.get(GeometryType.LOD3, None)

    @property
    def mesh(self):
        """Return LOD0 geometry."""
        return self.geometry.get(GeometryType.MESH, None)

    @property
    def volume_mesh(self):
        """Return LOD0 geometry."""
        return self.geometry.get(GeometryType.VOLUME_MESH, None)
