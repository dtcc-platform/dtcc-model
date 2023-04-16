from dataclasses import dataclass
import numpy as np
from dtcc_model import dtcc_pb2 as proto
from typing import Union, Tuple


@dataclass
class Pointcloud:
    points: np.ndarray = np.empty((0, 3), dtype=np.float64)
    classification: np.ndarray = np.empty((0, 1), dtype=np.uint8)
    intensity: np.ndarray = np.empty((0, 1), dtype=np.uint16)
    return_number: np.ndarray = np.empty((0, 1), dtype=np.uint8)
    number_of_returns: np.ndarray = np.empty((0, 1), dtype=np.uint8)
    crs: str = ""
    origin: Tuple[float, float] = (0, 0)
    bounds: Tuple[float, float, float, float] = (0, 0, 0, 0)

    def __str__(self):
        return f"Pointcloud with {self.points.shape[0]} points"

    def __len__(self):
        return self.points.shape[0]

    def used_classifications(self) -> set:
        return set(np.unique(self.classification))

    def from_proto(self, proto_pointcloud: Union[proto.PointCloud, bytes]):
        pass

    def to_proto(self) -> proto.PointCloud:
        pass
