# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

from dataclasses import dataclass, field

from dtcc_model.model import Model
from dtcc_model.geometry import Geometry
from collections import defaultdict
from uuid import uuid4


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
        List of child objects.
    parents : list
        List of parent objects.
    geometry : dict
        Dictionary of geometries.
    """

    id: str = field(default_factory=lambda: str(uuid4()))
    attributes: dict = field(default_factory=dict)
    children: dict = field(default_factory=lambda: defaultdict(list))
    parents: list = field(default_factory=list)
    geometry: dict = field(default_factory=dict)

    def defined_geometries(self):
        """Return a list of the types of geometries
        defined on this object."""
        return sorted(list(self.geometry.keys()))

    def definted_attributes(self):
        """Return a list of the attributes defined on this object."""
        return sorted(list(self.attributes.keys()))
