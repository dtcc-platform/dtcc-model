# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import numpy as np
from typing import Union
from dataclasses import dataclass, field

from . import dtcc_pb2 as proto


@dataclass
class Mesh:
    vertices: np.ndarray = field(default_factory=lambda: np.empty(0))
    normals: np.ndarray = field(default_factory=lambda: np.empty(0))
    faces: np.ndarray = field(default_factory=lambda: np.empty(0))

    def __str__(self):
        return f'DTCC Mesh with {len(self.vertices)} vertices, {len(self.normals)} normal(s), and {len(self.faces)} face(s)'

    @property
    def num_vertices(self) -> int:
        return len(self.vertices)

    @property
    def num_normals(self) -> int:
        return len(self.normals)

    @property
    def num_faces(self) -> int:
        return len(self.faces)

    def from_proto(self, pb: Union[proto.Mesh, bytes]):
        if isinstance(pb, bytes):
            pb = proto.Mesh.FromString(pb)
        self.vertices = np.array(pb.vertices).reshape((-1, 3))
        self.normals = np.array(pb.normals).reshape((-1, 3))
        self.faces = np.array(pb.faces).reshape((-1, 3))

    def to_proto(self) -> proto.Mesh:
        pb = proto.Mesh()
        pb.vertices.extend(self.vertices.flatten())
        pb.normals.extend(self.normals.flatten())
        pb.faces.extend(self.faces.flatten())
        return pb


@dataclass
class VolumeMesh:
    vertices: np.ndarray = field(default_factory=lambda: np.empty(0))
    cells: np.ndarray = field(default_factory=lambda: np.empty(0))

    def __str__(self):
        return f'DTCC VolumeMesh with {len(self.vertices)} vertices and {len(self.cells)} cell(s)'

    @ property
    def num_vertices(self) -> int:
        return len(self.vertices)

    @ property
    def num_cells(self) -> int:
        return len(self.cells)

    def from_proto(self, pb: Union[proto.VolumeMesh, bytes]):
        if isinstance(pb, bytes):
            pb = proto.VolumeMesh.FromString(pb)
        self.vertices = np.array(pb.vertices).reshape((-1, 3))
        self.cells = np.array(pb.cells).reshape((-1, 4))

    def to_proto(self) -> proto.Mesh:
        pb = proto.VolumeMesh()
        pb.vertices.extend(self.vertices.flatten())
        pb.cells.extend(self.cells.flatten())
        return pb
