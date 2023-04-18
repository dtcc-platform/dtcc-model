from dataclasses import dataclass, field
import numpy as np
from typing import Tuple, Union
import dtcc_model.dtcc_pb2 as proto
from affine import Affine


@dataclass
class GridField2D:
    grid: np.ndarray = field(default_factory=lambda: np.empty((0, 2), dtype=np.float64))
    transform: Affine = field(default_factory=lambda: Affine.identity())
    crs: str = ""

    @property
    def height(self) -> float:
        return self.grid.shape[1]

    @property
    def width(self) -> float:
        return self.grid.shape[0]

    @property
    def cell_size(self) -> Tuple[float, float]:
        return (abs(self.transform.a), abs(self.transform.e))

    @property
    def origin(self) -> Tuple[float, float]:
        return (self.transform.c, self.transform.f)

    @property
    def bounds(self) -> Tuple[float, float, float, float]:
        return (
            self.transform.c,
            self.transform.f + self.transform.e * self.grid.shape[1],
            self.transform.c + self.transform.a * self.grid.shape[0],
            self.transform.f,
        )

    def get_value(self, x: float, y: float) -> float:
        row, col = self.transform * (x, y)
        return self.grid[int(row), int(col)]

    def __str__(self):
        return f"GridField2D: {self.height} x {self.width}, with cell size {self.cell_size}"

    def to_proto(self):
        _proto_gridfield = proto.GridField2D()
        _proto_gridfield.values.extend(self.grid.flatten().tolist())
        _proto_gridfield.grid.xSize = self.grid.shape[0]
        _proto_gridfield.grid.ySize = self.grid.shape[1]
        _proto_gridfield.grid.xStep = self.cell_size[0]
        _proto_gridfield.grid.yStep = self.cell_size[1]
        _proto_gridfield.grid.boundingBox.p.x = self.bounds[0]
        _proto_gridfield.grid.boundingBox.p.y = self.bounds[1]
        _proto_gridfield.grid.boundingBox.q.x = self.bounds[2]
        _proto_gridfield.grid.boundingBox.q.y = self.bounds[3]

        return _proto_gridfield

    def from_proto(self, proto_grid: Union[proto.GridField2D, bytes]):
        if isinstance(proto_grid, bytes):
            _grid = proto.GridField2D()
            _grid.ParseFromString(proto_grid)
            proto_grid = _grid
        self.grid = np.array(proto_grid.values).reshape(
            proto_grid.grid.xSize, proto_grid.grid.ySize
        )
        self.transform = Affine(
            -proto_grid.grid.xStep,
            0.0,
            proto_grid.grid.boundingBox.p.x,
            proto_grid.grid.yStep,
            0.0,
            proto_grid.grid.boundingBox.p.y,
        )
