# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

from dataclasses import dataclass, field

from dtcc_model.model import DTCCModel
from dtcc_model.geometry import Geometry


@dataclass
class Object(DTCCModel):
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

    id: str = ""
    attributes: dict = field(default_factory=dict)
    children: list = field(default_factory=list)
    parents: list = field(default_factory=list)
    geometry: dict = field(default_factory=dict)
