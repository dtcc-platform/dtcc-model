# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

from dataclasses import dataclass
from typing import Union
import numpy as np

from dtcc_model.model import Model
from dtcc_model import dtcc_pb2 as proto


@dataclass
class Bounds(Model):
    """Represents the boundaries of a rectangular region in the xy plane) with
    optional extension along the z-axis (depth)

    Attributes
    ----------
    xmin : float
        Minimum x-coordinate.
    ymin : float
        Minimum y-coordinate.
    xmax : float
        Maximum x-coordinate.
    ymax : float
        Maximum y-coordinate.
    zmin: float
        Minimum z-coordinate.
    zmax: float
        Maximum z-coordinate.
    """

    xmin: float = 0.0
    ymin: float = 0.0
    xmax: float = 0.0
    ymax: float = 0.0
    zmin: float = 0.0
    zmax: float = 0.0

    def __str__(self):
        """Returns a formatted string representation of the bounds."""
        return f"DTCC Bounds {self.bndstr}"

    def calculate_bounds(self):
        """Calculate the bounds of the object."""
        return self

    @property
    def bndstr(self) -> str:
        """Returns the bounds as a formatted string.

        Returns
        -------
        str
            Formatted string of bounds.
        """
        return f"[{self.xmin}, {self.xmax}] x [{self.ymin}, {self.ymax}]"

    @property
    def width(self) -> float:
        """Returns the width of the bounds (x-axis).

        Returns
        -------
        float
            Width of the bounds.
        """
        return self.xmax - self.xmin

    @property
    def height(self) -> float:
        """Returns the height of the bounds (y-axis).

        Returns
        -------
        float
            Height of the bounds.
        """
        return self.ymax - self.ymin

    @property
    def depth(self) -> float:
        """Returns the depth of the bounds (z-axis).

        Returns
        -------
        float
            Depth of the bounds.
        """
        return self.zmax - self.zmin

    @property
    def north(self) -> float:
        """Returns the northernmost coordinate.

        Returns
        -------
        float
            Northernmost y-coordinate.
        """
        return self.ymax

    @property
    def south(self) -> float:
        """Returns the southernmost coordinate.

        Returns
        -------
        float
            Southernmost y-coordinate.
        """
        return self.ymin

    @property
    def east(self) -> float:
        """Returns the easternmost coordinate.

        Returns
        -------
        float
            Easternmost x-coordinate.
        """
        return self.xmax

    @property
    def west(self) -> float:
        """Returns the westernmost coordinate.

        Returns
        -------
        float
            Westernmost x-coordinate.
        """
        return self.xmin

    @property
    def tuple(self) -> tuple:
        """Returns the bounds as a tuple.

        Returns
        -------
        tuple
            Tuple representation of bounds.
        """
        return (self.xmin, self.ymin, self.xmax, self.ymax)

    @property
    def area(self) -> float:
        """Returns the area enclosed by the bounds.

        Returns
        -------
        float
            Area of the bounds.
        """
        return self.width * self.height

    @property
    def volume(self) -> float:
        """Returns the volume enclosed by the bounds.

        Returns
        -------
        float
            Volume of the bounds.
        """
        return self.width * self.height * self.depth

    # FIXME: How to handle z-axis?
    @property
    def center(self) -> tuple:
        """Returns the center point of the bounds.

        Returns
        -------
        tuple
            Center point as (x, y).
        """
        return (self.xmin + self.width / 2, self.ymin + self.height / 2)

    # FIXME: How to handle z-axis?
    def buffer(self, distance: float):
        """Increases the size of the bounds by a specified distance.

        Parameters
        ----------
        distance : float
            The distance to expand the bounds by.
        """
        self.xmin -= distance
        self.ymin -= distance
        self.xmax += distance
        self.ymax += distance
        return self

    # FIXME: How to handle z-axis?
    def union(self, other):
        """Merges this bounds with another, taking the outermost bounds.

        Parameters
        ----------
        other : Bounds
            The other bounds to merge with.
        """
        self.xmin = min(self.xmin, other.xmin)
        self.ymin = min(self.ymin, other.ymin)
        self.xmax = max(self.xmax, other.xmax)
        self.ymax = max(self.ymax, other.ymax)
        return self

    # FIXME: How to handle z-axis?
    def intersect(self, other):
        """Modifies this bounds to be the intersection with another.

        Parameters
        ----------
        other : Bounds
            The other bounds to intersect with.
        """
        self.xmin = max(self.xmin, other.xmin)
        self.ymin = max(self.ymin, other.ymin)
        self.xmax = min(self.xmax, other.xmax)
        self.ymax = min(self.ymax, other.ymax)
        return self

    def to_proto(self):
        """Return a protobuf representation of the Bounds.

        Returns
        -------
        proto.Bounds
            A protobuf representation of the Bounds.
        """
        pb = proto.Bounds()
        pb.xmin = self.xmin
        pb.xmax = self.xmax
        pb.ymin = self.ymin
        pb.ymax = self.ymax
        pb.zmin = self.zmin
        pb.zmax = self.zmax
        return pb

    def from_proto(self, pb):
        """Initialize Bounds from a protobuf representation.

        Parameters
        ----------
        pb: Union[proto.Bounds, bytes]
            The protobuf message or its serialized bytes representation.
        """
        if isinstance(pb, bytes):
            pb = proto.Bounds.FromString(pb)
        self.xmin = pb.xmin
        self.xmax = pb.xmax
        self.ymin = pb.ymin
        self.ymax = pb.ymax
        self.zmin = pb.zmin
        self.zmax = pb.zmax
