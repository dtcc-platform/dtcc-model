# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

import numpy as np
from typing import Union
from dataclasses import dataclass, field

from . import dtcc_pb2 as proto
from .grid import Grid


@dataclass
class GridField:
    grid: Grid = field(default_factory=Grid)
    values: np.ndarray = field(default_factory=lambda: np.empty(0))

    def __str__(self):
        return f"DTCC GridField on {self.grid.bounds.bndstr} with {len(self.values)} values"

    # FIXME: Implement evalution operator as in dtcc-builder C++ class
    # def get_value(self, x: float, y: float) -> float:

    def from_proto(self, pb: Union[proto.GridField, bytes]):
        if isinstance(pb, bytes):
            pb = proto.GridField.FromString(pb)
        self.grid.from_proto(pb.grid)
        self.values = np.array(pb.values)

    def to_proto(self) -> proto.GridField:
        pb = proto.GridField()
        pb.grid.CopyFrom(self.grid.to_proto())
        pb.values.extend(self.values)
        return pb


@dataclass
class GridVectorField:
    grid: Grid = field(default_factory=Grid)
    values: np.ndarray = field(default_factory=lambda: np.empty(0))

    def __str__(self):
        return f"DTCC GridVectorField on {self.grid.bounds.bndstr} with {len(self.values)} values"

    def from_proto(self, pb: Union[proto.GridVectorField, bytes]):
        if isinstance(pb, bytes):
            pb = proto.GridVectorField.FromString(pb)
        self.grid.from_proto(pb.grid)
        self.values = np.array(pb.values).reshape((-1, 3))

    def to_proto(self) -> proto.GridField:
        pb = proto.GridField()
        pb.grid.CopyFrom(self.grid.to_proto())
        pb.values.extend(self.values.flatten())
        return pb
