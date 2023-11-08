# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import numpy as np
from typing import Union
from dataclasses import dataclass, field

from dtcc_model.model import Model
from dtcc_model import dtcc_pb2 as proto


@dataclass
class Quantity(Model):
    """Represents a physical quantity on a geometry.

    A quantity has a value and a unit of measurement and can represent e.g. physical properties such as a temperature or a velocity vector field.
    The quantity takes a value on each element of a geometry and the value
    may be either scalar or vector-valued.

    A quantity is defined in relation to a specific geometry of an object.
    The geometry is identified by its local name (key) as part of the object.

    Note: Consider extending this class to support tensor-valued quantities.

    Note: Consider making this into a base class and deriving scalar and vector
    quantities from it. For now we just have a single class for both.

    Attributes
    ----------
    name: str
        Name of the quantity.
    unit: str
        Unit of measurement of the quantity.
    geometry: str
        Name (key) of the geometry on which the quantity is defined.
    values: np.ndarray
        An array of values (scalar or vector-valued) of the quantity.
        The dimension is n x d, where n is the number of elements in the geometry and d is the dimension of the quantity.
    """

    name: str = ""
    unit: str = ""
    geometry: str = ""
    values: np.ndarray = field(default_factory=lambda: np.empty(0))


    @property
    def shape(self):
        """Return the value shape of the quantity."""
        return self.values.shape[1]

    def from_proto(self, pb: Union[proto.Quantity, bytes]):
        """Initialize the Quantity object from a Protocol Buffers message.

        This method populates the Quantity object's attributes based on the
        information in a Protocol Buffers message.

        Parameters
        ----------
        pb : Union[proto.Quantity, bytes]
            The Protocol Buffers message or its serialized bytes representation.

        """
        if isinstance(pb, bytes):
            pb = proto.Quantity.FromString(pb)
        #self.vertices = np.array(pb.vertices).reshape((-1, 3))
        #self.normals = np.array(pb.normals).reshape((-1, 3))
        #self.faces = np.array(pb.faces, dtype=np.int64).reshape((-1, 3))

    def to_proto(self) -> proto.Quantity:
        """Convert the Quantity object to a Protocol Buffers message.

        Returns
        -------
        proto.Quantity
            A Protocol Buffers message representing the Quantity object.

        """
        pb = proto.Quantity()
        #pb.vertices.extend(self.vertices.flatten())
        #pb.normals.extend(self.normals.flatten())
        #pb.faces.extend(self.faces.flatten())
        #return pb
