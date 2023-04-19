# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import numpy as np
from typing import Union
from dataclasses import dataclass, field

from . import dtcc_pb2 as proto
from .meshes import Mesh, VolumeMesh


@dataclass
class MeshField:
    mesh: Mesh = field(default_factory=Mesh)
    values: np.ndarray = field(default_factory=lambda: np.empty(()))

    def __str__(self):
        return f'DTCC MeshField with {len(self.values)} values'

    def from_proto(self, pb: Union[proto.MeshField, bytes]):
        if isinstance(pb, bytes):
            pb = proto.MeshField.FromString(pb)
        self.mesh.from_proto(pb.mesh)
        self.values = np.array(pb.values)

    def to_proto(self) -> proto.MeshField:
        pb = proto.MeshField()
        pb.mesh.CopyFrom(self.mesh.to_proto())
        pb.values.extend(self.values)
        return pb


@dataclass
class MeshVectorField:
    mesh: Mesh = field(default_factory=Mesh)
    values: np.ndarray = field(default_factory=lambda: np.empty(()))

    def __str__(self):
        return f'DTCC MeshVectorField with {len(self.values)} values'

    def from_proto(self, pb: Union[proto.MeshVectorField, bytes]):
        if isinstance(pb, bytes):
            pb = proto.MeshVectorField.FromString(pb)
        self.mesh.from_proto(pb.mesh)
        self.values = np.array(pb.values).reshape((-1, 3))

    def to_proto(self) -> proto.MeshVectorField:
        pb = proto.MeshVectorField()
        pb.mesh.CopyFrom(self.mesh.to_proto())
        pb.values.extend(self.values.flatten())
        return pb


@dataclass
class VolumeMeshField:
    mesh: Mesh = field(default_factory=Mesh)
    values: np.ndarray = field(default_factory=lambda: np.empty(()))

    def __str__(self):
        return f'DTCC VolumeMeshField with {len(self.values)} values'

    def from_proto(self, pb: Union[proto.VolumeMeshField, bytes]):
        if isinstance(pb, bytes):
            pb = proto.VolumeMeshField.FromString(pb)
        self.mesh.from_proto(pb.mesh)
        self.values = np.array(pb.values)

    def to_proto(self) -> proto.VolumeMeshField:
        pb = proto.VolumeMeshField()
        pb.mesh.CopyFrom(self.mesh.to_proto())
        pb.values.extend(self.values)
        return pb


@dataclass
class VolumeMeshVectorField:
    mesh: Mesh = field(default_factory=Mesh)
    values: np.ndarray = field(default_factory=lambda: np.empty(()))

    def __str__(self):
        return f'DTCC VolumeMeshVectorField with {len(self.values)} values'

    def from_proto(self, pb: Union[proto.VolumeMeshVectorField, bytes]):
        if isinstance(pb, bytes):
            pb = proto.VolumeMeshVectorField.FromString(pb)
        self.mesh.from_proto(pb.mesh)
        self.values = np.array(pb.values).reshape((-1, 3))

    def to_proto(self) -> proto.VolumeMeshVectorField:
        pb = proto.VolumeMeshVectorField()
        pb.mesh.CopyFrom(self.mesh.to_proto())
        pb.values.extend(self.values.flatten())
        return pb
