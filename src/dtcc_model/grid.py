# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import numpy as np
from typing import Union
from dataclasses import dataclass, field

from . import dtcc_pb2 as proto
from .geometry import Bounds


@dataclass
class Grid:
    bounds: Bounds = field(default_factory=Bounds)
    width: int = 0
    height: int = 0
    xstep: float = 0.0
    ystep: float = 0.0

    def __str__(self):
        return f'DTCC Grid on {self.bounds.bndstr} with {self.width} x {self.height} cells'

    @property
    def num_vertices(self) -> int:
        return (self.width + 1) * (self.height + 1)

    @property
    def num_cells(self) -> int:
        return self.width * self.height

    def from_proto(self, pb: Union[proto.Mesh, bytes]):
        if isinstance(pb, bytes):
            pb = proto.Grid.FromString(pb)
        self.bounds.from_proto(pb.bounds)
        self.width = pb.width
        self.height = pb.height
        self.xstep = pb.xstep
        self.ystep = pb.ystep

    def to_proto(self) -> proto.Mesh:
        pb = proto.Mesh()
        pb.bounds.CopyFrom(self.bounds.to_proto())
        pb.width = self.width
        pb.height = self.height
        pb.xstep = self.xstep
        pb.ystep = self.ystep
        return pb
