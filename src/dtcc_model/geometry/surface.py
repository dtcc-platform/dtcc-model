# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

import numpy as np
from typing import Union
from dataclasses import dataclass, field
from inspect import getmembers, isfunction, ismethod
from dtcc_model.geometry import Bounds
from shapely.geometry import Polygon

from .geometry import Geometry
from dtcc_model import dtcc_pb2 as proto


@dataclass
class Surface(Geometry):
    """Represents a planar surface in 3D."""

    vertices: np.ndarray = field(default_factory=lambda: np.empty(0))
    normal: np.ndarray = field(default_factory=lambda: np.empty(0))
    holes: list[np.ndarray] = field(default_factory=lambda: [])

    def calc_bounds(self):
        """Calculate the bounding box of the surface."""
        self.bounds = Bounds(
            np.min(self.vertices[:, 0]),
            np.min(self.vertices[:, 1]),
            np.max(self.vertices[:, 0]),
            np.max(self.vertices[:, 1]),
        )
        return self.bounds

    @property
    def xmin(self):
        return np.min(self.vertices[:, 0])

    @property
    def ymin(self):
        return np.min(self.vertices[:, 1])

    @property
    def zmin(self):
        return np.min(self.vertices[:, 2])

    @property
    def xmax(self):
        return np.max(self.vertices[:, 0])

    @property
    def ymax(self):
        return np.max(self.vertices[:, 1])

    @property
    def zmax(self):
        return np.max(self.vertices[:, 2])

    @property
    def centroid(self):
        return np.mean(self.vertices, axis=0)

    def calculate_normal(self) -> np.ndarray:
        """Calculate the normal of the surface."""
        if self.vertices.shape[0] < 3:
            raise ValueError("The surface must have at least 3 vertices.")
        self.normal = np.cross(
            self.vertices[1] - self.vertices[0], self.vertices[2] - self.vertices[0]
        )
        self.normal /= np.linalg.norm(self.normal)
        return self.normal

    def is_planar(self, tol=1e-5):
        """Check if the surface is planar."""
        if self.normal.shape != (3,):
            self.calculate_normal()
        return np.allclose(
            np.dot(self.vertices - self.vertices[0], self.normal), 0, atol=tol
        )

    def translate(self, x=0, y=0, z=0):
        """Translate the surface."""
        self.vertices += np.array([x, y, z])
        for hole in self.holes:
            hole += np.array([x, y, z])

    def set_z(self, z):
        """Set the z-coordinate of the surface."""
        self.vertices[:, 2] = z
        for hole in self.holes:
            hole[:, 2] = z

    def from_proto(self, pb):
        if isinstance(pb, bytes):
            pb = proto.Surface.FromString(pb)
        self.vertices = np.array(pb.vertices).reshape(-1, 3)
        self.normal = np.array([pb.normal.x, pb.normal.y, pb.normal.z])

    def to_polygon(self) -> Polygon:
        """Convert the surface to a Shapely Polygon."""
        return Polygon(self.vertices, self.holes)

    def to_proto(self):
        pb = proto.Surface()
        pb.vertices.extend(self.vertices.flatten())
        pb.normal = proto.Vector(x=self.normal[0], y=self.normal[1], z=self.normal[2])
        return pb

    def __str__(self) -> str:
        return f"DTCC Surface with {len(self.vertices)} vertices"


@dataclass
class MultiSurface(Geometry):
    """Represents a planar surfaces in 3D."""

    surfaces: list[Surface] = field(default_factory=list)

    def __len__(self):
        return len(self.surfaces)

    def merge(self, other):
        """Merge two MultiSurfaces."""
        if not isinstance(other, MultiSurface):
            raise ValueError("Can only merge with another MultiSurface.")
        self.surfaces.extend(other.surfaces)
        self.calc_bounds()
        return self

    def calc_bounds(self):
        """Calculate the bounding box of the surface."""
        if len(self.surfaces) == 0:
            return
        else:
            self.surfaces[0].calc_bounds()
            self.bounds = self.surfaces[0].bounds
        for s in self.surfaces[1:]:
            s.calc_bounds()
            self.bounds.union(s.bounds)

    def translate(self, x=0, y=0, z=0):
        """Translate the surface."""
        for s in self.surfaces:
            s.translate(x, y, z)

    def set_z(self, z):
        """Set the z-coordinate of the surface."""
        for s in self.surfaces:
            s.set_z(z)

    def to_proto(self):
        pb = proto.MultiSurface()
        pb.surfaces.extend([s.to_proto() for s in self.surfaces])
        return pb

    def from_proto(self, pb):
        if isinstance(pb, bytes):
            pb = proto.MultiSurface.FromString(pb)
        self.surfaces = [Surface().from_proto(s) for s in pb.surfaces]

    def __str__(self) -> str:
        return f"DTCC MultiSurface with {len(self.surfaces)} surfaces"
