# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

from dataclasses import dataclass, field

from dtcc_model.model import Model
from .bounds import Bounds
from .transform import Transform


@dataclass
class Geometry(Model):
    """Base class for all geometry classes.

    Geometry classes represent geometric objects such as point clouds,
    surfaces, polygons, and meshes. They are used to represent the geometry of
    city objects.

    All geometries are stored in a local coordinate system, which may be
    different for each geometry. The transform attribute is used to transform
    the geometry from the local coordinate system to a global coordinate system.

    Attributes
    ----------
    bounds : Bounds
        Bounding box of the geometry in the local coordinate system.
    transform : Transform
        Affine transform to a global coordinate system.
    """

    bounds: Bounds = field(default_factory=Bounds)
    transform: Transform = field(default_factory=Transform)
