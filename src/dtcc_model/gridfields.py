# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

import numpy as np
from typing import Union
from dataclasses import dataclass, field
from inspect import getmembers, isfunction, ismethod

from .model import DTCCModel
from . import dtcc_pb2 as proto
from .grid import Grid


@dataclass
class GridField(DTCCModel):
    """A GridField represents a scalar field associated with a grid.

    The GridField class represents a scalar field associated with a structured
    grid. It combines grid geometry with scalar values assigned to each grid
    cell or vertex.

    Attributes
    ----------
    grid : Grid
        The structured grid associated with the field.
    values : np.ndarray
        An array of scalar values assigned to grid vertices.

    """

    grid: Grid = field(default_factory=Grid)
    values: np.ndarray = field(default_factory=lambda: np.empty(0))

    def __str__(self):
        """Return a string representation of the DTCC GridField."""
        return f"DTCC GridField on {self.grid.bounds.bndstr} with {len(self.values)} values"

    # FIXME: Implement evalution operator as in dtcc-builder C++ class
    # def get_value(self, x: float, y: float) -> float:

    def from_proto(self, pb: Union[proto.GridField, bytes]):
        """Initialize the GridField object from a Protocol Buffers message.

        This method populates the GridField object's attributes based on the
        information in a Protocol Buffers message.

        Parameters
        ----------
        pb : Union[proto.GridField, bytes]
            The Protocol Buffers message or its serialized bytes representation.

        """
        if isinstance(pb, bytes):
            pb = proto.GridField.FromString(pb)
        self.grid.from_proto(pb.grid)
        self.values = np.array(pb.values)

    def to_proto(self) -> proto.GridField:
        """Convert the GridField object to a Protocol Buffers message.

        Returns
        -------
        proto.GridField
            A Protocol Buffers message representing the GridField object.

        """
        pb = proto.GridField()
        pb.grid.CopyFrom(self.grid.to_proto())
        pb.values.extend(self.values)
        return pb


@dataclass
class GridVectorField(DTCCModel):
    """A GridVectorField represents a vector field associated with a grid.

    The GridVectorField class represents a vector field associated with a
    structured grid. It combines grid geometry with vector values assigned to
    each grid cell or vertex.

    Attributes
    ----------
    grid : Grid
        The structured grid associated with the field.
    values : np.ndarray
        An array of vector values assigned to grid cells or vertices. Each
        vector is represented as an array of three components (x, y, z).
    """
    grid: Grid = field(default_factory=Grid)
    values: np.ndarray = field(default_factory=lambda: np.empty(0))

    def __str__(self):
        """Return a string representation of the DTCC GridVectorField."""
        return f"DTCC GridVectorField on {self.grid.bounds.bndstr} with {len(self.values)} values"

    def from_proto(self, pb: Union[proto.GridVectorField, bytes]):
        """Initialize the GridVectorField object from a Protocol Buffers message.

        This method populates the GridVectorField object's attributes based on
        the information in a Protocol Buffers message.

        Parameters
        ----------
        pb : Union[proto.GridVectorField, bytes]
            The Protocol Buffers message or its serialized bytes representation.

        """
        if isinstance(pb, bytes):
            pb = proto.GridVectorField.FromString(pb)
        self.grid.from_proto(pb.grid)
        self.values = np.array(pb.values).reshape((-1, 3))

    def to_proto(self) -> proto.GridField:
        """Convert the GridVectorField object to a Protocol Buffers message.

        Returns
        -------
        proto.GridField
            A Protocol Buffers message representing the GridVectorField object.

        """
        pb = proto.GridField()
        pb.grid.CopyFrom(self.grid.to_proto())
        pb.values.extend(self.values.flatten())
        return pb
