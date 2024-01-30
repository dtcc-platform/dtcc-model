# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import numpy as np
from typing import Union
from dataclasses import dataclass, field
from inspect import getmembers, isfunction, ismethod

from .geometry import Geometry
from dtcc_model import dtcc_pb2 as proto


@dataclass
class Mesh(Geometry):
    """Represents an unstructured triangular mesh in 3D.

    The Mesh class represents a 3D triangular mesh, which consists of vertices
    and triangular faces.

    Attributes
    ----------
    vertices : np.ndarray
        An array of vertices in 3D space.
    faces : np.ndarray
        An array of triangular faces defined by vertex indices.
    markers : np.ndarray
        An array of markers or labels associated with the faces.

    """

    vertices: np.ndarray = field(default_factory=lambda: np.empty(0, dtype=np.float64))
    faces: np.ndarray = field(default_factory=lambda: np.empty(0, dtype=np.int64))
    markers: np.ndarray = field(default_factory=lambda: np.empty(0))

    def __str__(self):
        """Return a string representation of the DTCC Mesh

        Returns
        -------
        str
            A string describing the Mesh object.

        """
        return f"DTCC Mesh with {len(self.vertices)} vertices and {len(self.faces)} face(s)"

    @property
    def num_vertices(self) -> int:
        """Get the number of vertices in the mesh.

        Returns
        -------
        int
            The number of vertices in the mesh.

        """
        return len(self.vertices)

    @property
    def num_faces(self) -> int:
        """Calculate the number of faces in the mesh.

        Returns
        -------
        int
            The number of faces in the mesh.

        """
        return len(self.faces)

    def from_proto(self, pb: Union[proto.Mesh, bytes]):
        """Initialize the Mesh object from a Protocol Buffers message.

        This method populates the Mesh object's attributes based on the
        information in a Protocol Buffers message.

        Parameters
        ----------
        pb : Union[proto.Mesh, bytes]
            The Protocol Buffers message or its serialized bytes representation.

        """
        if isinstance(pb, bytes):
            pb = proto.Mesh.FromString(pb)
        self.vertices = np.array(pb.vertices).reshape((-1, 3))
        self.faces = np.array(pb.faces, dtype=np.int64).reshape((-1, 3))

    def to_proto(self) -> proto.Mesh:
        """Convert the Mesh object to a Protocol Buffers message.

        Returns
        -------
        proto.Mesh
            A Protocol Buffers message representing the Mesh object.

        """
        pb = proto.Mesh()
        pb.vertices.extend(self.vertices.flatten())
        pb.faces.extend(self.faces.flatten())
        return pb


@dataclass
class VolumeMesh(Geometry):
    """Represents an unstructured tetrahedral mesh in 3D.

    The VolumeMesh class represents a 3D volumetric mesh, which consists of
    vertices and tetrahedral cells.

    Attributes
    ----------
    vertices : np.ndarray
        An array of vertices in 3D space.
    cells : np.ndarray
        An array of tetrahedral cells defined by vertex indices.
    markers : np.ndarray
        An array of markers or labels associated with th cells.

    """

    vertices: np.ndarray = field(default_factory=lambda: np.empty(0))
    cells: np.ndarray = field(default_factory=lambda: np.empty(0))
    markers: np.ndarray = field(default_factory=lambda: np.empty(0))

    def __str__(self):
        """Return a string representation of the DTCC VolumeMesh, containing the number of
        vertices and cells.

        Returns
        -------
        str
            A string describing the VolumeMesh object.

        """
        return f"DTCC VolumeMesh with {len(self.vertices)} vertices and {len(self.cells)} cell(s)"

    @property
    def num_vertices(self) -> int:
        """Get the number of vertices in the volume mesh.

        Returns
        -------
        int
            The number of vertices in the volume mesh.

        """
        return len(self.vertices)

    @property
    def num_cells(self) -> int:
        """Get the number of cells or elements in the volume mesh.

        Returns
        -------
        int
            The number of cells or elements in the volume mesh.

        """
        return len(self.cells)

    def from_proto(self, pb: Union[proto.VolumeMesh, bytes]):
        """Initialize the VolumeMesh object from a Protocol Buffers message.

        This method populates the VolumeMesh object's attributes based on the
        information in a Protocol Buffers message.

        Parameters
        ----------
        pb : Union[proto.VolumeMesh, bytes]
            The Protocol Buffers message or its serialized bytes representation.

        """
        if isinstance(pb, bytes):
            pb = proto.VolumeMesh.FromString(pb)
        self.vertices = np.array(pb.vertices).reshape((-1, 3))
        self.cells = np.array(pb.cells, dtype=np.int64).reshape((-1, 4))

    def to_proto(self) -> proto.Mesh:
        """Convert the VolumeMesh object to a Protocol Buffers message.

        Returns
        -------
        proto.Mesh
            A Protocol Buffers message representing the VolumeMesh object.

        """
        pb = proto.VolumeMesh()
        pb.vertices.extend(self.vertices.flatten())
        pb.cells.extend(self.cells.flatten())
        return pb
