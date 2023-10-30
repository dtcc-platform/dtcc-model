# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

import numpy as np
from typing import Union
from dataclasses import dataclass, field
from inspect import getmembers, isfunction, ismethod


from .model import DTCCModel
from . import dtcc_pb2 as proto


@dataclass
class Surface(DTCCModel):
    """A 3D planar surface."""

    vertices: np.ndarray = field(default_factory=lambda: np.empty(0))
    normal: np.ndarray = field(default_factory=lambda: np.empty(0))

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

    def from_proto(self, pb):
        if isinstance(pb, bytes):
            pb = proto.Surface.FromString(pb)
        self.vertices = np.array(pb.vertices).reshape(-1, 3)
        self.normal = np.array([pb.normal.x, pb.normal.y, pb.normal.z])

    def to_proto(self):
        pb = proto.Surface()
        pb.vertices.extend(self.vertices.flatten())
        pb.normal = proto.Vector(x=self.normal[0], y=self.normal[1], z=self.normal[2])
        return pb

    def __str__(self) -> str:
        return f"DTCC Surface with {len(self.vertices)} vertices"


class MultiSurface(DTCCModel):
    """A collection of 3D planar surface."""

    surfaces: list[Surface] = field(default_factory=lambda: [])

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
