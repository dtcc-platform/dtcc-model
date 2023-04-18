# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

from dataclasses import dataclass, field
import numpy as np
from dtcc_model import dtcc_pb2 as proto


@dataclass
class Mesh:
    vertices: np.ndarray = field(default_factory=lambda: np.empty())
    normals: np.ndarray = field(default_factory=lambda: np.empty())
    faces: np.ndarray = field(default_factory=lambda: np.empty())

    def __repr__(self):
        return f'DTCC Mesh with {len(self.vertices)} vertices, {len(self.normals)} normal(s), and {len(self.faces)} face(s)'

    def num_vertices(self):
        return len(self.vertices)

    def num_normals(self):
        return len(self.normals)

    def num_faces(self):
        return len(self.faces)

    def from_proto(self, proto_mesh: proto.Mesh):
        'Convert from proto.Mesh'
        if isinstance(proto_mesh, bytes):
            proto_mesh = proto.Mesh.FromString(proto_mesh)
        self.vertices = np.array(proto_mesh.vertices).reshape((-1, 3))
        self.normals = np.array(proto_mesh.normals).reshape((-1, 3))
        self.faces = np.array(proto_mesh.faces).reshape((-1, 3))

    def to_proto(self) -> proto.Mesh:
        'Convert to proto.Mesh'
        assert self.vertices.ndim == 2 and np.shape(self.vertices)[1] == 3
        assert self.normals.ndim == 2 and np.shape(self.normals)[1] == 3
        assert self.faces.ndim == 2 and np.shape(self.faces)[1] == 3
        proto_mesh = proto.Mesh()
        proto_mesh.vertices.extend(self.vertices.flatten())
        proto_mesh.normals.extend(self.normals.flatten())
        proto_mesh.faces.extend(self.faces.flatten())
        return proto_mesh
