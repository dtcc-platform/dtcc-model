# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

from dataclasses import dataclass, field
import numpy as np
from dtcc_model import dtcc_pb2 as proto


@dataclass
class VolumeMesh:
    vertices: np.ndarray = field(default_factory=lambda: np.empty())
    cells: np.ndarray = field(default_factory=lambda: np.empty())

    def num_vertices(self):
        return len(self.vertices)

    def num_cells(self):
        return len(self.cells)

    def __repr__(self):
        return f'DTCC VolumeMesh with {len(self.vertices)} vertices and {len(self.cells)} cell(s)'

    def from_proto(self, proto_volume_mesh: proto.Mesh):
        'Convert from proto.VolumeMesh'
        if isinstance(proto_volume_mesh, bytes):
            proto_volumemesh = proto.VolumeMesh.FromString(proto_volume_mesh)
        self.vertices = np.array(proto_volume_mesh.vertices).reshape((-1, 3))
        self.cells = np.array(proto_volume_mesh.cells).reshape((-1, 4))

    def to_proto(self) -> proto.Mesh:
        'Convert to proto.VolumeMesh'
        assert self.vertices.ndim == 2 and np.shape(self.vertices)[1] == 3
        assert self.cells.ndim == 2 and np.shape(self.cells)[1] == 4
        proto_volume_mesh = proto.VolumeMesh()
        proto_volume_mesh.vertices.extend(self.vertices.flatten())
        proto_volume_mesh.cells.extend(self.cells.flatten())
        return proto_volume_mesh
