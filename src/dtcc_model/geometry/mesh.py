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

    def calculate_bounds(self):
        """Calculate the bounding box of the mesh."""
        self.bounds = Bounds(
            np.min(self.vertices[:, 0]),
            np.min(self.vertices[:, 1]),
            np.min(self.vertices[:, 2]),
            np.max(self.vertices[:, 0]),
            np.max(self.vertices[:, 1]),
            np.max(self.vertices[:, 2]),
        )
        return self.bounds

    @property
    def num_faces(self) -> int:
        """Calculate the number of faces in the mesh.

        Returns
        -------
        int
            The number of faces in the mesh.

        """
        return len(self.faces)

    def to_proto(self) -> proto.Geometry:
        """Return a protobuf representation of the Mesh.

        Returns
        -------
        proto.Geometry
            A protobuf representation of the Mesh as a Geometry.
        """

        # Handle Geometry fields
        pb = Geometry.to_proto(self)

        # Handle specific fields
        _pb = proto.Mesh()
        _pb.vertices.extend(self.vertices.flatten())
        _pb.faces.extend(self.faces.flatten())
        pb.mesh.CopyFrom(_pb)

        return pb

    def from_proto(self, pb: Union[proto.Geometry, bytes]):
        """Initialize Mesh from a protobuf representation.

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
        _pb = pb.mesh
        self.vertices = np.array(_pb.vertices).reshape((-1, 3))
        self.faces = np.array(_pb.faces, dtype=np.int64).reshape((-1, 3))


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

    def to_proto(self) -> proto.Geometry:
        """Return a protobuf representation of the VolumeMesh.

        Returns
        -------
        proto.Geometry
            A protobuf representation of the VolumeMesh as a Geometry.
        """

        # Handle Geometry fields
        pb = Geometry.to_proto(self)

        # Handle specific fields
        _pb = proto.VolumeMesh()
        _pb.vertices.extend(self.vertices.flatten())
        _pb.cells.extend(self.cells.flatten())
        pb.mesh.CopyFrom(_pb)

        return pb

    def from_proto(self, pb: Union[proto.Geometry, bytes]):
        """Initialize VolumeMesh from a protobuf representation.

        Parameters
        ----------
        pb: Union[proto.Geometry, bytes]
            The protobuf message or its serialized bytes representation.
        """

        # Handle byte representation
        if isinstance(pb, bytes):
            pb = proto.FromString(pb)

        # Handle Geometry fields
        Geometry.from_proto(self, pb)

        # Handle specific fields
        _pb = pb.volume_mesh
        self.vertices = np.array(_pb.vertices).reshape((-1, 3))
        self.cells = np.array(_pb.faces, dtype=np.int64).reshape((-1, 4))
