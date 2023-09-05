# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import numpy as np
from typing import Union
from dataclasses import dataclass, field
from inspect import getmembers, isfunction, ismethod

from .model import DTCCModel
from . import dtcc_pb2 as proto
from .meshes import Mesh, VolumeMesh


@dataclass
class MeshField(DTCCModel):

    """A MeshField represents a scalar field associated with a Mesh.

    The MeshField class represents a scalar field associated with a 3D Mesh.
    It includes the Mesh object and an array of scalar values associated with
    each vertex in the mesh.

    Attributes
    ----------
    mesh : Mesh
        The Mesh object to which the scalar field is associated.
    values : np.ndarray
        An array of scalar values associated with each vertex in the mesh.

    """

    mesh: Mesh = field(default_factory=Mesh)
    values: np.ndarray = field(default_factory=lambda: np.empty(0))

    def __str__(self):
        """Return a string representation of the DTCC MeshField.

        Returns
        -------
        str
            A string describing the MeshField object.

        """
        return f"DTCC MeshField with {len(self.values)} values"

    def from_proto(self, pb: Union[proto.MeshField, bytes]):
        """Initialize the MeshField object from a Protocol Buffers message.

        This method populates the MeshField object's attributes based on the
        information in a Protocol Buffers message.

        Parameters
        ----------
        pb : Union[proto.MeshField, bytes]
            The Protocol Buffers message or its serialized bytes representation.

        """
        if isinstance(pb, bytes):
            pb = proto.MeshField.FromString(pb)
        self.mesh.from_proto(pb.mesh)
        self.values = np.array(pb.values)

    def to_proto(self) -> proto.MeshField:
        """Convert the MeshField object to a Protocol Buffers message.

        Returns
        -------
        proto.MeshField
            A Protocol Buffers message representing the MeshField object.

        """
        pb = proto.MeshField()
        pb.mesh.CopyFrom(self.mesh.to_proto())
        pb.values.extend(self.values)
        return pb


@dataclass
class MeshVectorField:

    """A MeshVectorField represents a vector field associated with a Mesh.

    The MeshVectorField class represents a vector field associated with a 3D Mesh.
    It includes the Mesh object and an array of vector values associated with
    each vertex in the mesh. Each vector has three components (x, y, and z).

    Attributes
    ----------
    mesh : Mesh
        The Mesh object to which the vector field is associated.
    values : np.ndarray
        An array of vector values associated with each vertex in the mesh.

    """

    mesh: Mesh = field(default_factory=Mesh)
    values: np.ndarray = field(default_factory=lambda: np.empty(0))

    def __str__(self):
        """Return a string representation of the DTCC MeshVectorField.

        Returns
        -------
        str
            A string describing the MeshVectorField object.

        """
        return f"DTCC MeshVectorField with {len(self.values)} values"

    def from_proto(self, pb: Union[proto.MeshVectorField, bytes]):
        """Initialize the MeshVectorField object from a Protocol Buffers message.

        This method populates the MeshVectorField object's attributes based on the
        information in a Protocol Buffers message.

        Parameters
        ----------
        pb : Union[proto.MeshVectorField, bytes]
            The Protocol Buffers message or its serialized bytes representation.

        """
        if isinstance(pb, bytes):
            pb = proto.MeshVectorField.FromString(pb)
        self.mesh.from_proto(pb.mesh)
        self.values = np.array(pb.values).reshape((-1, 3))

    def to_proto(self) -> proto.MeshVectorField:
        """Convert the MeshVectorField object to a Protocol Buffers message.

        Returns
        -------
        proto.MeshVectorField
            A Protocol Buffers message representing the MeshVectorField object.

        """
        pb = proto.MeshVectorField()
        pb.mesh.CopyFrom(self.mesh.to_proto())
        pb.values.extend(self.values.flatten())
        return pb


@dataclass
class VolumeMeshField(DTCCModel):

    """A VolumeMeshField represents a scalar field associated with a VolumeMesh.

    The VolumeMeshField class represents a scalar field associated with a 3D
    VolumeMesh. It includes the VolumeMesh object and an array of scalar values
    associated with each vertex in the mesh.

    Attributes
    ----------
    mesh : Mesh
        The VolumeMesh object to which the scalar field is associated.
    values : np.ndarray
        An array of scalar values associated with each vertex in the mesh.

    """
    
    mesh: Mesh = field(default_factory=Mesh)
    values: np.ndarray = field(default_factory=lambda: np.empty(0))

    def __str__(self):
        """Return a string representation of the DTCC VolumeMeshField.

        Returns
        -------
        str
            A string describing the VolumeMeshField object.

        """
        return f"DTCC VolumeMeshField with {len(self.values)} values"

    def from_proto(self, pb: Union[proto.VolumeMeshField, bytes]):
        """Initialize the VolumeMeshField object from a Protocol Buffers message.

        This method populates the VolumeMeshField object's attributes based on the
        information in a Protocol Buffers message.

        Parameters
        ----------
        pb : Union[proto.VolumeMeshField, bytes]
            The Protocol Buffers message or its serialized bytes representation.
        """
        if isinstance(pb, bytes):
            pb = proto.VolumeMeshField.FromString(pb)
        self.mesh.from_proto(pb.mesh)
        self.values = np.array(pb.values)

    def to_proto(self) -> proto.VolumeMeshField:
        """Convert the VolumeMeshField object to a Protocol Buffers message.

        Returns
        -------
        proto.VolumeMeshField
            A Protocol Buffers message representing the VolumeMeshField object.

        """
        pb = proto.VolumeMeshField()
        pb.mesh.CopyFrom(self.mesh.to_proto())
        pb.values.extend(self.values)
        return pb


@dataclass
class VolumeMeshVectorField(DTCCModel):

    """A VolumeMeshVectorField represents a vector field associated with a VolumeMesh.

    The VolumeMeshVectorField class represents a vector field associated with a 3D
    VolumeMesh. It includes the VolumeMesh object and an array of vector values
    associated with each vertex in the mesh. Each vector has three components (x, y, z).

    Attributes
    ----------
    mesh : Mesh
        The VolumeMesh object to which the vector field is associated.
    values : np.ndarray
        An array of vector values associated with each vertex in the mesh.

    """

    mesh: Mesh = field(default_factory=Mesh)
    values: np.ndarray = field(default_factory=lambda: np.empty(0))

    def __str__(self):
        """Return a string representation of the DTCC VolumeMeshVectorField.

        Returns
        -------
        str
            A string describing the VolumeMeshVectorField object.

        """
        return f"DTCC VolumeMeshVectorField with {len(self.values)} values"

    def from_proto(self, pb: Union[proto.VolumeMeshVectorField, bytes]):
        """Initialize the VolumeMeshVectorField object from a Protocol Buffers message.

        This method populates the VolumeMeshVectorField object's attributes based on the
        information in a Protocol Buffers message.

        Parameters
        ----------
        pb : Union[proto.VolumeMeshVectorField, bytes]
            The Protocol Buffers message or its serialized bytes representation.

        """
        if isinstance(pb, bytes):
            pb = proto.VolumeMeshVectorField.FromString(pb)
        self.mesh.from_proto(pb.mesh)
        self.values = np.array(pb.values).reshape((-1, 3))

    def to_proto(self) -> proto.VolumeMeshVectorField:
        """Convert the VolumeMeshVectorField object to a Protocol Buffers message.

        Returns
        -------
        proto.VolumeMeshVectorField
            A Protocol Buffers message representing the VolumeMeshVectorField object.

        """
        pb = proto.VolumeMeshVectorField()
        pb.mesh.CopyFrom(self.mesh.to_proto())
        pb.values.extend(self.values.flatten())
        return pb
