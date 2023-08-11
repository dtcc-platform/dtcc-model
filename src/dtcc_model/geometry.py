# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import numpy as np
from typing import Union
from dataclasses import dataclass
from inspect import getmembers, isfunction, ismethod

from .model import DTCCModel
from . import dtcc_pb2 as proto


@dataclass
class Bounds(DTCCModel):
    """
    A class representing spatial bounds.

    Attributes
    ----------
    xmin : float
        The minimum x-coordinate.
    ymin : float
        The minimum y-coordinate.
    xmax : float
        The maximum x-coordinate.
    ymax : float
        The maximum y-coordinate.
    """

    xmin: float = 0.0
    ymin: float = 0.0
    xmax: float = 0.0
    ymax: float = 0.0

    def __str__(self):
        """
        Returns a string representation of the Bounds instance.

        Returns
        -------
        str
            A string detailing the bounds.
        """
        return f"DTCC Bounds {self.bndstr}"

    @property
    def bndstr(self) -> str:
        """Returns the bounds as a string in format: [xmin, xmax] x [ymin, ymax]."""
        return f"[{self.xmin}, {self.xmax}] x [{self.ymin}, {self.ymax}]"

    @property
    def width(self) -> float:
        """Returns the width of the bounds."""
        return self.xmax - self.xmin

    @property
    def height(self) -> float:
        """Returns the height of the bounds."""
        return self.ymax - self.ymin

    @property
    def north(self) -> float:
        """Returns the northernmost coordinate (ymax)."""
        return self.ymax

    @property
    def south(self) -> float:
        """Returns the southernmost coordinate (ymin)."""
        return self.ymin

    @property
    def east(self) -> float:
        """Returns the easternmost coordinate (xmax)."""
        return self.xmax

    @property
    def west(self) -> float:
        """Returns the westernmost coordinate (xmin)."""
        return self.xmin

    @property
    def tuple(self) -> tuple:
        """Returns the bounds as a tuple (xmin, ymin, xmax, ymax)."""
        return (self.xmin, self.ymin, self.xmax, self.ymax)

    @property
    def area(self) -> float:
        """Returns the area covered by the bounds."""
        return self.width * self.height

    def center(self) -> tuple:
        """Returns the center point of the bounds."""
        return (self.xmin + self.width / 2, self.ymin + self.height / 2)

    def buffer(self, distance: float):
        """
        Expands the bounds by the given distance in all directions.

        Parameters
        ----------
        distance : float
            The distance to expand the bounds by.
        """
        self.xmin -= distance
        self.ymin -= distance
        self.xmax += distance
        self.ymax += distance

    def union(self, other):
        """
        Modifies the bounds to be the union of itself and another Bounds object.

        Parameters
        ----------
        other : Bounds
            The other bounds to union with.
        """
        self.xmin = min(self.xmin, other.xmin)
        self.ymin = min(self.ymin, other.ymin)
        self.xmax = max(self.xmax, other.xmax)
        self.ymax = max(self.ymax, other.ymax)

    def intersect(self, other):
        """
        Modifies the bounds to be the intersection of itself and another Bounds object.

        Parameters
        ----------
        other : Bounds
            The other bounds to intersect with.
        """
        self.xmin = max(self.xmin, other.xmin)
        self.ymin = max(self.ymin, other.ymin)
        self.xmax = min(self.xmax, other.xmax)
        self.ymax = min(self.ymax, other.ymax)

    def from_proto(self, pb: Union[proto.Bounds, bytes]):
        """
        Sets the bounds from a protobuf message or bytes.

        Parameters
        ----------
        pb : Union[proto.Bounds, bytes]
            The protobuf message or its byte representation.
        """
        if isinstance(pb, bytes):
            pb = proto.Bounds.FromString(pb)
        self.xmin = pb.xmin
        self.xmax = pb.xmax
        self.ymin = pb.ymin
        self.ymax = pb.ymax

    def to_proto(self) -> proto.Bounds:
        pb = proto.Bounds()
        pb.xmin = self.xmin
        pb.xmax = self.xmax
        pb.ymin = self.ymin
        pb.ymax = self.ymax
        return pb


@dataclass
class Georef(DTCCModel):
    """
    A class representing geospatial reference information.

    Attributes
    ----------
    crs : str
        The coordinate reference system identifier (e.g., 'EPSG:4326').
    epsg : int
        The EPSG code corresponding to the coordinate reference system.
    x0 : float
        The x-coordinate of the reference origin.
    y0 : float
        The y-coordinate of the reference origin.
    """

    crs: str = ""
    epsg: int = 0
    x0: float = 0.0
    y0: float = 0.0

    def __str__(self):
        """
        Returns a string representation of the Georef instance.

        Returns
        -------
        str
            A string detailing the geospatial reference information.
        """
        return (
            f"DTCC Georef {self.crs} ({self.epsg}) with origin ({self.x0}, {self.y0})"
        )

    def from_proto(self, pb: Union[proto.Georef, bytes]):
        """
        Sets the geospatial reference information from a protobuf message or bytes.

        Parameters:
        -----------
        pb : Union[proto.Georef, bytes]
            The protobuf message or its byte representation.
        """
        if isinstance(pb, bytes):
            pb = proto.Georef.FromString(pb)
        self.crs = pb.crs
        self.epsg = pb.epsg
        self.x0 = pb.x0
        self.y0 = pb.y0

    def to_proto(self) -> proto.Georef:
        """
        Converts the geospatial reference information to a protobuf message.

        Returns
        -------
        proto.Georef
            The protobuf representation of the geospatial reference information.
        """
        pb = proto.Georef()
        pb.crs = self.crs
        pb.epsg = self.epsg
        pb.x0 = self.x0
        pb.y0 = self.y0
        return pb
