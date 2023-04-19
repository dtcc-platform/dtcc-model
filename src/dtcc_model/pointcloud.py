# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import numpy as np
from typing import Union
from dataclasses import dataclass, field

from . import dtcc_pb2 as proto
from .geometry import Bounds, Georef


@dataclass
class PointCloud:
    bounds: Bounds = field(default_factory=Bounds)
    georef: Georef = field(default_factory=Georef)
    points: np.ndarray = field(default_factory=lambda: np.empty(()))
    classification: np.ndarray = field(default_factory=lambda: np.empty(()))
    intensity: np.ndarray = field(default_factory=lambda: np.empty(()))
    return_number: np.ndarray = field(default_factory=lambda: np.empty(()))
    num_returns: np.ndarray = field(default_factory=lambda: np.empty(()))

    def __str__(self):
        return f'DTCC PointCloud on {self.bounds.bndstr} with {len(self.points)} points'

    def __len__(self):
        return self.points.shape[0]

    def used_classifications(self) -> set:
        return set(np.unique(self.classification))

    def calculate_bounds(self):
        self.bounds.xmin = self.points[:, 0].min()
        self.bounds.xmax = self.points[:, 0].max()
        self.bounds.ymin = self.points[:, 1].min()
        self.bounds.ymax = self.points[:, 1].max()

    def remove_points(self, indices: np.ndarray):
        self.points = np.delete(self.points, indices, axis=0)
        if len(self.classification) > 0:
            self.classification = np.delete(
                self.classification, indices, axis=0)
        if len(self.intensity) > 0:
            self.intensity = np.delete(self.intensity, indices, axis=0)
        if len(self.return_number) > 0:
            self.return_number = np.delete(self.return_number, indices, axis=0)
        if len(self.num_of_returns) > 0:
            self.num_of_returns = np.delete(
                self.num_of_returns, indices, axis=0)

    def from_proto(self, pb: Union[proto.PointCloud, bytes]):
        if isinstance(pb, bytes):
            pb.PointCloud.FromString(pb)
        self.bounds.from_proto(pb.bounds)
        self.georef.from_proto(pb.georef)
        self.points = np.array(pb.points).reshape(-1, 3)
        self.classification = np.array(pb.classification).astype(np.uint8)
        self.intensity = np.array(pb.intensity).astype(np.uint16)
        self.return_number = np.array(pb.returnNumber).astype(np.uint8)
        self.num_returns = np.array(pb.num_returns).astype(np.uint8)

    def to_proto(self) -> proto.PointCloud:
        pb = proto.PointCloud()
        pb.bounds.CopyFrom(self.bounds.to_proto())
        pb.georef.CopyFrom(self.georef.to_proto())
        pb.points.extend(self.points.flatten())
        pb.classification.extend(self.classification)
        pb.intensity.extend(self.intensity)
        pb.return_number.extend(self.return_number)
        pb.num_returns.extend(self.num_returns)
        return pb
