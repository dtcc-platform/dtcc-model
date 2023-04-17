# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

from dataclasses import dataclass
import numpy as np
from dtcc_model import dtcc_pb2 as proto


@dataclass
class Mesh:
    vertices: np.ndarray = np.empty((0, 3), dtype=np.float64)
    normals: np.ndarray = np.empty((0, 3), dtype=np.float64)
    faces: np.ndarray = np.empty((0, 3), dtype=np.uint32)

    def __repr__(self):
        return f'DTCC Mesh with {len(self.vertices)} vertices, {len(self.normals)} normal(s), and {len(self.faces)} face(s)'

    def from_proto(self, proto_mesh: proto.Mesh):
        'Convert from proto.Mesh'
        self.vertices = np.array([(v.x, v.y, v.z)
                                 for v in proto_mesh.vertices])
        self.normals = np.array([(n.x, n.y, n.z)
                                 for n in proto_mesh.normals])
        self.faces = np.array([(f.v0, f.v1, f.v2)
                              for f in proto_mesh.faces])

    def to_proto(self) -> proto.Mesh:
        'Convert to proto.Mesh'
        assert self.vertices.ndim == 2 and np.shape(self.vertices)[1] == 3
        assert self.normals.ndim == 2 and np.shape(self.normals)[1] == 3
        assert self.faces.ndim == 2 and np.shape(self.faces)[1] == 3
        _vertices = [proto.Vector3D(x=x, y=y, z=z)
                     for x, y, z in self.vertices]
        _normals = [proto.Vector3D(x=x, y=y, z=z)
                    for x, y, z in self.normals]
        _faces = [proto.Triangle(v0=v0, v1=v1, v2=v2)
                  for v0, v1, v2 in self.faces]
        proto_mesh = proto.Mesh()
        proto_mesh.vertices.extend(_vertices)
        proto_mesh.normals.extend(_normals)
        proto_mesh.faces.extend(_faces)
        return proto_mesh

# FIXME: isinstance(proto_mesh, bytes)
# FIXME: proto_mesh.vertices.extend(self.vertices.flatten())
