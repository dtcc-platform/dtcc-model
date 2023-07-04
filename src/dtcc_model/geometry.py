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
    xmin: float = 0.0
    ymin: float = 0.0
    xmax: float = 0.0
    ymax: float = 0.0

    def __str__(self):
        return f"DTCC Bounds {self.bndstr}"

    @property
    def bndstr(self) -> str:
        return f"[{self.xmin}, {self.xmax}] x [{self.ymin}, {self.ymax}]"

    @property
    def width(self) -> float:
        return self.xmax - self.xmin

    @property
    def height(self) -> float:
        return self.ymax - self.ymin

    @property
    def north(self) -> float:
        return self.ymax

    @property
    def south(self) -> float:
        return self.ymin

    @property
    def east(self) -> float:
        return self.xmax

    @property
    def west(self) -> float:
        return self.xmin

    @property
    def tuple(self) -> tuple:
        return (self.xmin, self.ymin, self.xmax, self.ymax)

    @property
    def area(self) -> float:
        return self.width * self.height

    def center(self) -> tuple:
        return (self.xmin + self.width / 2, self.ymin + self.height / 2)

    def buffer(self, distance: float):
        self.xmin -= distance
        self.ymin -= distance
        self.xmax += distance
        self.ymax += distance

    def union(self, other):
        self.xmin = min(self.xmin, other.xmin)
        self.ymin = min(self.ymin, other.ymin)
        self.xmax = max(self.xmax, other.xmax)
        self.ymax = max(self.ymax, other.ymax)

    def intersect(self, other):
        self.xmin = max(self.xmin, other.xmin)
        self.ymin = max(self.ymin, other.ymin)
        self.xmax = min(self.xmax, other.xmax)
        self.ymax = min(self.ymax, other.ymax)

    def from_proto(self, pb: Union[proto.Bounds, bytes]):
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
    crs: str = ""
    epsg: int = 0
    x0: float = 0.0
    y0: float = 0.0

    def __str__(self):
        return (
            f"DTCC Georef {self.crs} ({self.epsg}) with origin ({self.x0}, {self.y0})"
        )

    def from_proto(self, pb: Union[proto.Georef, bytes]):
        if isinstance(pb, bytes):
            pb = proto.Georef.FromString(pb)
        self.crs = pb.crs
        self.epsg = pb.epsg
        self.x0 = pb.x0
        self.y0 = pb.y0

    def to_proto(self) -> proto.Georef:
        pb = proto.Georef()
        pb.crs = self.crs
        pb.epsg = self.epsg
        pb.x0 = self.x0
        pb.y0 = self.y0
        return pb
