# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

import numpy as np
from typing import Union
from dataclasses import dataclass, field
from inspect import getmembers, isfunction, ismethod
from dtcc_model.geometry import Bounds
from shapely.geometry import Polygon
from shapely.validation import make_valid
from dtcc_model.logging import info, warning, error, debug
from .geometry import Geometry
from dtcc_model import dtcc_pb2 as proto


@dataclass
class Surface(Geometry):
    """Represents a planar surface in 3D."""

    vertices: np.ndarray = field(default_factory=lambda: np.empty(0))
    normal: np.ndarray = field(default_factory=lambda: np.empty(0))
    holes: list[np.ndarray] = field(default_factory=lambda: [])

    def calculate_bounds(self):
        """Calculate the bounding box of the surface."""
        if len(self.vertices) == 0:
            return Bounds()
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

    def to_polygon(self, simplify=1e-2) -> Polygon:
        """Convert the surface to a Shapely Polygon."""
        if len(self.vertices) < 3:
            # warning("Surface has less than 3 vertices.")
            return Polygon()
        p = Polygon(self.vertices[:, :2], self.holes)
        if not p.is_valid:
            p = make_valid(p)
        if not p.is_valid and p.geom_type != "Polygon":
            warning("Cannot convert surface to valid polygon.")
            return Polygon()
        if simplify > 0:
            p = p.simplify(simplify, True)
        return p

    def from_polygon(self, polygon: Polygon, height=0):
        """Convert a Shapely Polygon to a surface."""
        verts = np.array(polygon.exterior.coords)[
            :-1, :2
        ]  # remove last duplicate vertex
        self.vertices = np.hstack((verts, np.full((verts.shape[0], 1), height)))
        for hole in polygon.interiors:
            hole_verts = np.array(hole.coords)[:, :2]
            hole_verts = np.hstack(
                [hole_verts, np.full((hole_verts.shape[0], 1), height)]
            )
            self.holes.append(hole_verts)
        self.calculate_bounds()
        return self

    def to_proto(self):
        pb = proto.Surface()
        pb.vertices.extend(self.vertices.flatten())
        for hole in self.holes:
            hole_pb = proto.LineString()
            hole_pb.vertices.extend(hole.flatten())
            pb.holes.append(hole_pb)
        # pb.normal = proto.Vector(x=self.normal[0], y=self.normal[1], z=self.normal[2])
        return pb

    def from_proto(self, pb):
        if isinstance(pb, bytes):
            pb = proto.Surface.FromString(pb)
        self.vertices = np.array(pb.vertices).reshape(-1, 3)
        self.holes = []
        for hole in pb.holes:
            self.holes.append(np.array(hole.vertices).reshape(-1, 3))

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
        self.calculate_bounds()
        return self

    def calculate_bounds(self):
        """Calculate the bounding box of the surface."""
        if len(self.surfaces) == 0:
            return
        else:
            self.surfaces[0].calculate_bounds()
            self.bounds = self.surfaces[0].bounds
        for s in self.surfaces[1:]:
            s.calculate_bounds()
            self.bounds.union(s.bounds)

    @property
    def zmax(self):
        return max([s.zmax for s in self.surfaces])

    def translate(self, x=0, y=0, z=0):
        """Translate the surface."""
        for s in self.surfaces:
            s.translate(x, y, z)

    def set_z(self, z):
        """Set the z-coordinate of the surface."""
        for s in self.surfaces:
            s.set_z(z)

    def centroid(self):
        """Get the centroid of the MultiSurface."""
        return np.mean([s.centroid for s in self.surfaces], axis=0)

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
