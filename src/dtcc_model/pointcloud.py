from dataclasses import dataclass
import numpy as np
from dtcc_model import dtcc_pb2 as proto
from typing import Union, Tuple


@dataclass
class Pointcloud:
    points: np.ndarray = np.empty((0, 3), dtype=np.float64)
    classification: np.ndarray = np.empty((0), dtype=np.uint8)
    intensity: np.ndarray = np.empty((0), dtype=np.uint16)
    return_number: np.ndarray = np.empty((0), dtype=np.uint8)
    number_of_returns: np.ndarray = np.empty((0), dtype=np.uint8)
    crs: str = ""
    origin: Tuple[float, float] = (0, 0)
    bounds: Tuple[float, float, float, float] = (0, 0, 0, 0)

    def __str__(self):
        return f"Pointcloud with {self.points.shape[0]} points"

    def __len__(self):
        return self.points.shape[0]

    def used_classifications(self) -> set:
        return set(np.unique(self.classification))

    def calc_bounds(self):
        self.bounds = (
            self.points[:, 0].min(),
            self.points[:, 1].min(),
            self.points[:, 0].max(),
            self.points[:, 1].max(),
        )

    def remove_points(self, indices: np.ndarray):
        self.points = np.delete(self.points, indices, axis=0)
        if len(self.classification) > 0:
            self.classification = np.delete(self.classification, indices, axis=0)
        if len(self.intensity) > 0:
            self.intensity = np.delete(self.intensity, indices, axis=0)
        if len(self.return_number) > 0:
            self.return_number = np.delete(self.return_number, indices, axis=0)
        if len(self.number_of_returns) > 0:
            self.number_of_returns = np.delete(self.number_of_returns, indices, axis=0)

    def from_proto(self, proto_pointcloud: Union[proto.PointCloud, bytes]):
        if isinstance(proto_pointcloud, bytes):
            _pointcloud = proto.PointCloud()
            _pointcloud.ParseFromString(proto_pointcloud)
            proto_pointcloud = _pointcloud
        self.points = np.array(proto_pointcloud.points).reshape(-1, 3)
        self.classification = np.array(proto_pointcloud.classification).astype(np.uint8)
        self.intensity = np.array(proto_pointcloud.intensity).astype(np.uint16)
        self.return_number = np.array(proto_pointcloud.returnNumber).astype(np.uint8)
        self.number_of_returns = np.array(proto_pointcloud.numReturns).astype(np.uint8)
        self.bounds = (
            proto_pointcloud.bounds.p.x,
            proto_pointcloud.bounds.p.y,
            proto_pointcloud.bounds.q.x,
            proto_pointcloud.bounds.q.y,
        )
        self.origin = (
            proto_pointcloud.georeference.x0,
            proto_pointcloud.georeference.y0,
        )
        self.crs = proto_pointcloud.georeference.crs

    def to_proto(self) -> proto.PointCloud:
        proto_pc = proto.PointCloud()
        proto_pc.points.extend(self.points.reshape(-1).tolist())
        proto_pc.classification.extend(self.classification.reshape(-1).tolist())
        proto_pc.intensity.extend(self.intensity.reshape(-1).tolist())
        proto_pc.returnNumber.extend(self.return_number.reshape(-1).tolist())
        proto_pc.numReturns.extend(self.number_of_returns.reshape(-1).tolist())
        proto_pc.bounds.p.x = self.bounds[0]
        proto_pc.bounds.p.y = self.bounds[1]
        proto_pc.bounds.q.x = self.bounds[2]
        proto_pc.bounds.q.y = self.bounds[3]
        proto_pc.georeference.x0 = self.origin[0]
        proto_pc.georeference.y0 = self.origin[1]
        proto_pc.georeference.crs = self.crs
        return proto_pc
