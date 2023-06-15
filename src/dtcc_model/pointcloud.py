# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import numpy as np
from typing import Union, ClassVar
from dataclasses import dataclass, field


from . import dtcc_pb2 as proto
from .model import DTCCModel
from .geometry import Bounds, Georef


@dataclass
class PointCloud(DTCCModel):
    """A point cloud is a set of points with associated attributes.
    Attributes:
      bounds (Bounds): The bounds of the point cloud.
      georef (Georef): The georeference of the point cloud.
      points (np.ndarray): The points of the point cloud as (n,3) dimensional numpy array.

      The following attributes are as defined in the las specification:
      classification (np.ndarray): The classification of the points as (n,) dimensional numpy array.
      intensity (np.ndarray): The intensity of the points as (n,) dimensional numpy array.
      return_number (np.ndarray): The return number of the points as (n,) dimensional numpy array.
      num_returns (np.ndarray): The number of returns of the points as (n,) dimensional numpy array.


    """

    bounds: Bounds = field(default_factory=Bounds)
    georef: Georef = field(default_factory=Georef)
    points: np.ndarray = field(default_factory=lambda: np.empty(0))
    classification: np.ndarray = field(default_factory=lambda: np.empty(0))
    intensity: np.ndarray = field(default_factory=lambda: np.empty(0))
    return_number: np.ndarray = field(default_factory=lambda: np.empty(0))
    num_returns: np.ndarray = field(default_factory=lambda: np.empty(0))

    def __str__(self):
        return f"DTCC PointCloud on {self.bounds.bndstr} with {len(self.points)} points"

    def __len__(self):
        return self.points.shape[0]

    def used_classifications(self) -> set:
        return set(np.unique(self.classification))

    def calculate_bounds(self):
        """Calculate the bounds of the point cloud and update the bounds attribute."""
        self.bounds.xmin = self.points[:, 0].min()
        self.bounds.xmax = self.points[:, 0].max()
        self.bounds.ymin = self.points[:, 1].min()
        self.bounds.ymax = self.points[:, 1].max()

    def remove_points(self, indices: np.ndarray):
        """Remove points from the point cloud using the given indices."""
        self.points = np.delete(self.points, indices, axis=0)
        if len(self.classification) > 0:
            self.classification = np.delete(self.classification, indices, axis=0)
        if len(self.intensity) > 0:
            self.intensity = np.delete(self.intensity, indices, axis=0)
        if len(self.return_number) > 0:
            self.return_number = np.delete(self.return_number, indices, axis=0)
        if len(self.num_returns) > 0:
            self.num_returns = np.delete(self.num_returns, indices, axis=0)

    def from_proto(self, pb: Union[proto.PointCloud, bytes]):
        if isinstance(pb, bytes):
            pb.PointCloud.FromString(pb)
        self.bounds.from_proto(pb.bounds)
        self.georef.from_proto(pb.georef)
        self.points = np.array(pb.points).reshape(-1, 3)
        self.classification = np.array(pb.classification).astype(np.uint8)
        self.intensity = np.array(pb.intensity).astype(np.uint16)
        self.return_number = np.array(pb.return_number).astype(np.uint8)
        self.num_returns = np.array(pb.num_returns).astype(np.uint8)

    def to_proto(self) -> proto.PointCloud:
        pb = proto.PointCloud()
        pb.bounds.CopyFrom(self.bounds.to_proto())
        pb.georef.CopyFrom(self.georef.to_proto())
        pb.points.extend(self.points.flatten())
        if len(self.classification) > 0:
            pb.classification.extend(self.classification)
        if len(self.intensity) > 0:
            pb.intensity.extend(self.intensity)
        if len(self.return_number) > 0:
            pb.return_number.extend(self.return_number)
        if len(self.num_returns) > 0:
            pb.num_returns.extend(self.num_returns)
        return pb
