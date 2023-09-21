# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

import numpy as np
from typing import Union
from dataclasses import dataclass, field
from affine import Affine
from dtcc_model.geometry import Bounds
from logging import info, warning, error
from .model import DTCCModel
from . import dtcc_pb2 as proto


@dataclass
class Raster(DTCCModel):

    """
    A georeferenced n-dimensional raster of values.

    This class represents a georeferenced n-dimensional raster of values, where `data` is a
    NumPy array of shape (height, width, channels) or (height, width) if `channels` is 1.

    Attributes
    ----------
    data : np.ndarray
        The data of the raster as a NumPy array.
    georef : Affine
        The georeference of the raster.
    nodata : float
        The value representing nodata or missing data.
    crs : str
        The coordinate reference system (CRS) information.

    """

    data: np.ndarray = field(default_factory=lambda: np.empty(()))
    georef: Affine = field(default_factory=Affine.identity)
    nodata: float = np.nan
    crs: str = ""

    def __str__(self):
        """
        Return a string representation of the Raster.

        Returns
        -------
        str
            A string representation of the Raster.

        """
        return f"DTCC Raster with {self.data.shape} values"

    @property
    def shape(self):
        """
        Get the shape of the raster data.

        Returns
        -------
        tuple
            A tuple representing the shape of the raster data.

        """
        return self.data.shape

    @property
    def height(self):
        """
        Get the height (number of rows) of the raster data.

        Returns
        -------
        int
            The height of the raster data.

        """
        if len(self.data.shape) < 2:
            return 0
        return self.data.shape[0]

    @property
    def width(self):
        """
        Get the width (number of columns) of the raster data.

        Returns
        -------
        int
            The width of the raster data.

        """
        if len(self.data.shape) < 2:
            return 0
        return self.data.shape[1]

    @property
    def channels(self):
        """
        Get the number of channels in the raster data.

        Returns
        -------
        int
            The number of channels in the raster data.

        """
        if len(self.data.shape) < 2:
            return 0
        if len(self.data.shape) == 2:
            return 1
        else:
            return self.data.shape[2]

    @property
    def bounds(self):
        """
        Get the spatial bounds of the raster.

        Returns
        -------
        Bounds
            The spatial bounds of the raster.

        """
        return Bounds(
            xmin=self.georef.c,
            ymin=self.georef.f + self.georef.e * self.height,
            xmax=self.georef.c + self.georef.a * self.width,
            ymax=self.georef.f,
        )

    @property
    def cell_size(self):
        """
        Get the cell size (pixel size) of the raster.

        Returns
        -------
        tuple
            A tuple containing the horizontal and vertical cell sizes.

        """
        return (self.georef.a, self.georef.e)

    def get_value(self, x: float, y: float):
        """
        Get the value at the given coordinate.

        Parameters
        ----------
        x : float
            The x-coordinate.
        y : float
            The y-coordinate.

        Returns
        -------
        data
            The value at the given coordinate.

        """
        col, row = ~self.georef * (x, y)
        try:
            data = self.data[int(row), int(col)]
        except IndexError:
            error_str = f"IndexError in get_value at ({x}, {y})"
            error_str += f"\ncol: {col}, row: {row}"
            error_str += f"\ngeoref: {self.georef}"
            error_str += f"\nshape: {self.data.shape}"
            error(error_str)
            raise
            # data = self.nodata
        return data

    def to_proto(self) -> proto.Raster:
        """
        Convert the Raster object to a protobuf representation.

        Returns
        -------
        proto.Raster
            A protobuf representation of the Raster.

        """
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
        """
        Initialize the Raster object from a protobuf representation.

        Parameters
        ----------
        pb : Union[proto.Raster, bytes]
            A protobuf representation of the Raster or a bytes object.

        Returns
        -------
        None

        """
        if isinstance(pb, bytes):
            _raster = proto.Raster()
            _raster.FromString(pb)
            pb = _raster

        if pb.height == 0 or pb.width == 0 or pb.channels == 0:
            self.data = np.empty(())
        elif pb.channels == 1:
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
