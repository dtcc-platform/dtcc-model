# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

from dataclasses import dataclass
from typing import Union
import numpy as np

from dtcc_model.model import DTCCModel
from dtcc_model import dtcc_pb2 as proto

# FIXME: REMOVE THIS CLASS (replaced by Transform)


@dataclass
class Georef(DTCCModel):
    """Represents georeferencing information for spatial data.

    Attributes
    ----------
    crs : str
        Coordinate reference system string.
    epsg : int
        EPSG code corresponding to the coordinate reference system.
    x0 : float
        x-coordinate of the origin.
    y0 : float
        y-coordinate of the origin.
    """

    crs: str = ""
    epsg: int = 0
    x0: float = 0.0
    y0: float = 0.0

    def __str__(self):
        """Returns a formatted string representation of the georeferencing information."""
        return (
            f"DTCC Georef {self.crs} ({self.epsg}) with origin ({self.x0}, {self.y0})"
        )

    def from_proto(self, pb: Union[proto.Georef, bytes]):
        """Loads the georeferencing information from a protobuf representation.

        Parameters
        ----------
        pb : Union[proto.Georef, bytes]
            The protobuf representation or bytes.
        """
        if isinstance(pb, bytes):
            pb = proto.Georef.FromString(pb)
        self.crs = pb.crs
        self.epsg = pb.epsg
        self.x0 = pb.x0
        self.y0 = pb.y0

    def to_proto(self) -> proto.Georef:
        """Converts the georeferencing information to a protobuf representation.

        Returns
        -------
        proto.Georef
            Protobuf representation of the georeferencing information.
        """
        pb = proto.Georef()
        pb.crs = self.crs
        pb.epsg = self.epsg
        pb.x0 = self.x0
        pb.y0 = self.y0
        return pb
