# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import numpy as np
from typing import Union
from dataclasses import dataclass, field
from inspect import getmembers, isfunction, ismethod

from .model import DTCCModel
from . import dtcc_pb2 as proto


@dataclass
class Mesh(DTCCModel):
    """A Mesh represents a 3D triangular mesh.

    The Mesh class represents a 3D triangular mesh, which consists of vertices,
    vertex colors, normals, faces, face colors, and markers. It is commonly
    used for representing complex 3D geometries in computer graphics and
    simulation.

    Attributes
    ----------
    vertices : np.ndarray
        An array of vertices in 3D space.
    vertex_colors : np.ndarray
        An array of colors associated with each vertex.
    normals : np.ndarray
        An array of normal vectors for each vertex.
    faces : np.ndarray
        An array of triangular faces defined by vertex indices.
    face_colors : np.ndarray
        An array of colors associated with each face.
    markers : np.ndarray
        An array of markers or labels associated with mesh elements.

    """
    vertices: np.ndarray = field(default_factory=lambda: np.empty(0))
    vertex_colors: np.ndarray = field(default_factory=lambda: np.empty(0))
    normals: np.ndarray = field(default_factory=lambda: np.empty(0))
    faces: np.ndarray = field(default_factory=lambda: np.empty(0))
    face_colors: np.ndarray = field(default_factory=lambda: np.empty(0))
    markers: np.ndarray = field(default_factory=lambda: np.empty(0))

    def __str__(self):
        """Return a string representation of the DTCC Mesh, containing the number of vertices,
        normals and faces.

        Returns
        -------
        str
            A string describing the Mesh object.

        """
        return f"DTCC Mesh with {len(self.vertices)} vertices, {len(self.normals)} normal(s), and {len(self.faces)} face(s)"

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
    def num_normals(self) -> int:
        """Get the number of normal vectors in the mesh.

        Returns
        -------
        int
            The number of normal vectors in the mesh.

        """
        return len(self.normals)

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
        self.normals = np.array(pb.normals).reshape((-1, 3))
        self.faces = np.array(pb.faces).reshape((-1, 3))

    def to_proto(self) -> proto.Mesh:
        """Convert the Mesh object to a Protocol Buffers message.

        Returns
        -------
        proto.Mesh
            A Protocol Buffers message representing the Mesh object.

        """
        pb = proto.Mesh()
        pb.vertices.extend(self.vertices.flatten())
        pb.normals.extend(self.normals.flatten())
        pb.faces.extend(self.faces.flatten())
        return pb


@dataclass
class VolumeMesh(DTCCModel):
    """A VolumeMesh represents a 3D volumetric mesh.

    The VolumeMesh class represents a 3D volumetric mesh, which consists of
    vertices, tetrahedral cells, and markers. It is used for representing
    three-dimensional finite element meshes in scientific simulations.

    Attributes
    ----------
    vertices : np.ndarray
        An array of vertices in 3D space.
    cells : np.ndarray
        An array of cells or elements defined by vertex indices.
    markers : np.ndarray
        An array of markers or labels associated with mesh elements.

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
        self.cells = np.array(pb.cells).reshape((-1, 4))

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
