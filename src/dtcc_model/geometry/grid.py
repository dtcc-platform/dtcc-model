# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

from dataclasses import dataclass
from typing import Union
import numpy as np


from .geometry import Geometry
from dtcc_model import proto


@dataclass
class Grid(Geometry):
    """Represents a structured quadrilateral grid in 2D.

    Attributes
    ----------
    width : int
        Number of cells in the x-direction (horizontal).
    height : int
        Number of cells in the y-direction (vertical).
    """

    width: int = 0
    height: int = 0

    def __str__(self):
        return (
            f"DTCC Grid on {self.bounds.bndstr} with {self.width} x {self.height} cells"
        )

    @property
    def xstep(self) -> int:
        """Return the distance between adjacent grid points in the x-direction.

        Returns
        -------
        int
            The distance between adjacent grid points in the x-direction.

        """
        return self.bounds.width / self.width

    @property
    def ystep(self) -> int:
        """Return the distance between adjacent grid points in the y-direction.

        Returns
        -------
        int
            The distance between adjacent grid points in the y-direction.

        """
        return self.bounds.height / self.height

    @property
    def num_vertices(self) -> int:
        """Return the total number of vertices in the grid.

        Returns
        -------
        int
            The total number of vertices in the grid, including boundary vertices.

        """
        return (self.width + 1) * (self.height + 1)

    @property
    def num_cells(self) -> int:
        """Return the total number of cells in the grid.

        Returns
        -------
        int
            The total number of cells in the grid.

        """
        return self.width * self.height

    def coordinates(self):
        """Return the coordinates of the grid points.

        Returns
        -------
        np.ndarray
            An array of shape (num_vertices, 2) containing the coordinates of the grid points.

        """
        x = np.linspace(self.bounds.xmin, self.bounds.xmax, self.width + 1)
        y = np.linspace(self.bounds.ymin, self.bounds.ymax, self.height + 1)
        X, Y = np.meshgrid(x, y)
        return np.vstack([X.ravel(), Y.ravel()]).T

    def to_proto(self) -> proto.Geometry:
        """Return a protobuf representation of the Grid.

        Returns
        -------
        proto.Geometry
            A protobuf representation of the Grid as a Geometry.
        """

        # Handle Geometry fields
        pb = Geometry.to_proto(self)

        # Handle specific fields
        _pb = proto.Grid()
        _pb.width = self.width
        _pb.height = self.height
        pb.grid.CopyFrom(_pb)

        return pb

    def from_proto(self, pb: Union[proto.Geometry, bytes]):
        """Initialize Grid from a protobuf representation.

        Parameters
        ----------
        pb: Union[proto.Geometry, bytes]
            The protobuf message or its serialized bytes representation.
        """

        # Handle byte representation
        if isinstance(pb, bytes):
            pb = proto.Geometry.FromString(pb)

        # Handle Geometry fields
        Geometry.from_proto(self, pb)

        # Handle specific fields
        _pb = pb.grid
        self.width = _pb.width
        self.height = _pb.height


@dataclass
class VolumeGrid(Geometry):
    """Represents a structured hexahedral grid in 3D.

    Attributes
    ----------
    width : int
        Number of cells in the x-direction.
    height : int
        Number of cells in the y-direction.
    depth : int
        Number of cells in the z-direction.
    """

    width: int = 0
    height: int = 0
    depth: int = 0

    def __str__(self):
        return f"DTCC VolumeGrid on {self.bounds.bndstr} with {self.width} x {self.height} x {self.depth} cells"

    @property
    def xstep(self) -> int:
        """Return the distance between adjacent grid points in the x-direction.

        Returns
        -------
        int
            The distance between adjacent grid points in the x-direction.

        """
        return self.bounds.width / self.width

    @property
    def ystep(self) -> int:
        """Return the distance between adjacent grid points in the y-direction.

        Returns
        -------
        int
            The distance between adjacent grid points in the y-direction.

        """
        return self.bounds.height / self.height

    @property
    def zstep(self) -> int:
        """Return the distance between adjacent grid points in the z-direction.

        Returns
        -------
        int
            The distance between adjacent grid points in the z-direction.

        """
        return self.bounds.depth / self.depth

    @property
    def num_vertices(self) -> int:
        """Return the total number of vertices in the grid.

        Returns
        -------
        int
            The total number of vertices in the grid, including boundary vertices.

        """
        return (self.width + 1) * (self.height + 1) * (self.depth + 1)

    @property
    def num_cells(self) -> int:
        """Return the total number of cells in the grid.

        Returns
        -------
        int
            The total number of cells in the grid.

        """
        return self.width * self.height * self.depth

    def coordinates(self):
        """Return the coordinates of the grid points.

        Returns
        -------
        np.ndarray
            An array of shape (num_vertices, 3) containing the coordinates of the grid points.

        """
        x = np.linspace(self.bounds.xmin, self.bounds.xmax, self.width + 1)
        y = np.linspace(self.bounds.ymin, self.bounds.ymax, self.height + 1)
        z = np.linspace(self.bounds.zmin, self.bounds.zmax, self.depth + 1)
        X, Y, Z = np.meshgrid(x, y, z)
        return np.vstack([X.ravel(), Y.ravel(), Z.ravel()]).T

    def to_proto(self) -> proto.Geometry:
        """Return a protobuf representation of the VolumeGrid.

        Returns
        -------
        proto.Geometry
            A protobuf representation of the VolumeGrid as a Geometry.
        """

        # Handle Geometry fields
        pb = Geometry.to_proto(self)

        # Handle specific fields
        _pb = proto.VolumeGrid()
        _pb.width = self.width
        _pb.height = self.height
        _pb.depth = self.depth
        pb.volume_grid.CopyFrom(_pb)

        return pb

    def from_proto(self, pb: Union[proto.Geometry, bytes]):
        """Initialize VolumeGrid from a protobuf representation.

        Parameters
        ----------
        pb: Union[proto.Geometry, bytes]
            The protobuf message or its serialized bytes representation.
        """

        # Handle byte representation
        if isinstance(pb, bytes):
            pb = proto.Geometry.FromString(pb)

        # Handle Geometry fields
        Geometry.from_proto(self, pb)

        # Handle specific fields
        _pb = pb.volume_grid
        self.width = _pb.width
        self.height = _pb.height
        self.depth = _pb.depth
