# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

import numpy as np
from typing import Union
from dataclasses import dataclass, field
from affine import Affine

from . import dtcc_pb2 as proto


@dataclass
class Raster:
    """A georeferenced n-dimensional raster of values.
    data is a numpy array of shape (height, width, channels) or (height, width)
    if channels is 1.
    """

    data: np.ndarray = field(default_factory=lambda: np.empty(()))
    georef: Affine = field(default_factory=Affine.identity)
    nodata: float = np.nan
    crs: str = ""

    def __str__(self):
        return f"DTCC Raster with {self.data.shape} values"

    @property
    def shape(self):
        return self.data.shape

    @property
    def height(self):
        return self.data.shape[0]

    @property
    def width(self):
        return self.data.shape[1]

    @property
    def channels(self):
        if len(self.data.shape) == 2:
            return 1
        else:
            return self.data.shape[2]

    @property
    def bounds(self):
        return (
            self.georef.c,
            self.georef.f + self.georef.e * self.width,
            self.georef.c + self.georef.a * self.height,
            self.georef.f,
        )

    @property
    def cell_size(self):
        return (self.georef.a, self.georef.e)

    def get_value(self, x: float, y: float):
        """Get the value at the given coordinate"""
        col, row = self.georef * (x, y)
        return self.data[int(row), int(col)]

    def to_proto(self) -> proto.Raster:
        pb = proto.Raster()
        pb.height = self.height
        pb.width = self.width
        pb.channels = self.channels
        pb.values.extend(self.data.flatten())
        pb.nodata = self.nodata
        pb.dtype = self.data.dtype.name

        pb.transform.a = self.georef.a
        pb.transform.b = self.georef.b
        pb.transform.c = self.georef.c
        pb.transform.d = self.georef.d
        pb.transform.e = self.georef.e
        pb.transform.f = self.georef.f

        return pb

    def from_proto(self, pb: Union[proto.Raster, bytes]):
        if isinstance(pb, bytes):
            _raster = proto.Raster()
            _raster.FromString(pb)
            pb = _raster

        if pb.channels == 1:
            self.data = self.data.reshape((pb.height, pb.width))
        else:
            self.data = np.array(pb.values).reshape((pb.height, pb.width, pb.channels))
        if pb.dtype:
            self.data = self.data.astype(pb.dtype)
        self.nodata = pb.nodata
        self.georef = Affine(
            pb.transform.a,
            pb.transform.b,
            pb.transform.c,
            pb.transform.d,
            pb.transform.e,
            pb.transform.f,
        )
