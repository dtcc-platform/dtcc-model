# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

from dataclasses import dataclass, field
from collections import defaultdict
from enum import Enum, auto

from dtcc_model.logging import info, warning, error
from dtcc_model.model import Model
from dtcc_model.geometry import Geometry, Bounds
from collections import defaultdict
from uuid import uuid4
from dtcc_model.quantity import Quantity


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

    id: str = field(default_factory=lambda: str(uuid4()))
    attributes: dict = field(default_factory=dict)
    children: dict = field(default_factory=lambda: defaultdict(list))
    parents: dict = field(default_factory=lambda: defaultdict(list))
    geometry: dict = field(default_factory=dict)
    quantities: list[Quantity] = field(default_factory=list)

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

    @property
    def point_cloud(self):
        """Return POINT_CLOUD geometry."""
        return self.geometry.get(GeometryType.POINT_CLOUD, None)

    @property
    def raster(self):
        """Return RASTER geometry."""
        return self.geometry.get(GeometryType.RASTER, None)

    @property
    def bounds(self):
        """Return BOUNDS geometry."""
        bounds = self.geometry.get(GeometryType.BOUNDS, None)
        if bounds is None:
            bounds = self.calculate_bounds()
        return bounds

    def add_geometry(self, geometry: Geometry, geometry_type: GeometryType):
        """Add geometry to object."""
        if not isinstance(geometry_type, GeometryType):
            warning(f"Invalid geometry type (but I'll allow it): {geometry_type}")
        self.geometry[geometry_type] = geometry

    def add_quantity(self, quantity):
        """Add quantity to object."""
        if not quantity.geometry in self.geometry:
            error(f"Unable to add quantity; missing geometry: {quantity.geometry}")
        self.quantities.append(quantity)

    def add_child(self, child):
        """Add child object."""
        if not isinstance(child, Object):
            raise ValueError(f"Invalid child object: {child}")
        self.children[type(child)].append(child)
        child.parents[type(self)].append(self)

    def add_children(self, children):
        """Adds a list of children objects."""
        for child in children:
            self.add_child(child)

    def flatten_geometry(self, geom_type: GeometryType):
        """Returns a single geometry of the specified type, merging all the geometries of the children."""
        geom = self.geometry.get(geom_type, None)
        child_list = list(self.children)
        for child_list in self.children.values():
            for child in child_list:
                child_geom = child.geometry.get(geom_type, None)
                if geom is None and child_geom is not None:
                    geom = child_geom
                if child_geom is not None:
                    geom.merge(child_geom)
        return geom

    def calculate_bounds(self, lod=None):
        """Calculate the bounding box of the object."""
        if lod is not None:
            lods = [lod]
        else:
            lods = list(GeometryType)
        bounds = None
        for lod in lods:
            geom = self.flatten_geometry(lod)
            if geom is not None:
                lod_bounds = geom.calculate_bounds()
                if bounds is None:
                    bounds = lod_bounds
                else:
                    bounds = bounds.union(lod_bounds)
        self.add_geometry(bounds, GeometryType.BOUNDS)
        return bounds

    def defined_geometries(self):
        """Return a list of the types of geometries
        defined on this object."""
        return sorted(list(self.geometry.keys()))

    def definted_attributes(self):
        """Return a list of the attributes defined on this object."""
        return sorted(list(self.attributes.keys()))
