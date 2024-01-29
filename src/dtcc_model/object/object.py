# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

from dataclasses import dataclass, field
from collections import defaultdict
from enum import Enum, auto

from dtcc_model.model import Model
from dtcc_model.geometry import Geometry

class GeometryType(Enum):
    LOD0 = auto()
    LOD1 = auto()
    LOD2 = auto()
    LOD3 = auto()
    MESH = auto()
    VOLUMEMESH = auto()
    POINTCLOUD = auto()
    RASTER = auto()




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
    children : list
        List of child objects (key is type).
    parents : list
        Dictionary of parent objects (key is type).
    geometry : dict
        Dictionary of geometries.
    """

    id: str = ""
    attributes: dict = field(default_factory=dict)
    children: list = field(default_factory=lambda: defaultdict(list))
    parents: list = field(default_factory=lambda: defaultdict(list))
    geometry: dict = field(default_factory=dict)

    @property
    def num_children(self):
        """Return number of child objects."""
        return len(self.children)

    @property
    def num_parents(self):
        """Return number of parent objects."""
        return len(self.parents)

    @property
    def lod0(self):
        """Return LOD0 geometry."""
        return self.geometry.get(GeometryType.LOD0, [])

    @property
    def lod1(self):
        """Return LOD0 geometry."""
        return self.geometry.get(GeometryType.LOD1, [])

    @property
    def lod2(self):
        """Return LOD0 geometry."""
        return self.geometry.get(GeometryType.LOD2, [])

    @property
    def lod3(self):
        """Return LOD0 geometry."""
        return self.geometry.get(GeometryType.LOD3, [])

    @property
    def mesh(self):
        """Return LOD0 geometry."""
        return self.geometry.get(GeometryType.MESH, [])

    @property
    def volumemesh(self):
        """Return LOD0 geometry."""
        return self.geometry.get(GeometryType.VOLUMEMESH, [])

