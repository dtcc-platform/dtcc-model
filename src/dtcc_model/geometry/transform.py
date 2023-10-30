# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

from dataclasses import dataclass, field
from typing import Union
import numpy as np

from dtcc_model.model import Model
from dtcc_model import dtcc_pb2 as proto


@dataclass
class Transform(Model):
    """Represents an affine transformation to a global coordinate system.

    The affine transformation is represented by a 4x4 matrix, where the
    upper-left 3x3 submatrix represents the rotation and scaling, and the last
    column represents the translation. By applying the affine transformation to
    the coordinates of a point in the local coordinate system, one obtains the
    coordinates of the point in the global coordinate system specified by the
    spatial reference system (SRS).

    Attributes
    ----------
    srs : str
        Name of global coordinate system (Spatial Reference System).
    affine: np.ndarray
        4x4 affine transformation matrix.
    """

    srs: str = ""
    affine: np.ndarray = field(default_factory=lambda: np.eye(4))

    def __call__(self, points):
        """
        Apply the affine transformation to a 3D point or an N x 3 array of points.

        Parameters
        ----------
        points: tuple/list or np.ndarray of shape (N, 3)
            Points to be transformed.

        Returns
        -------
        tuple/list or np.ndarray of shape (N, 3)
            Transformed points.
        """
        if isinstance(points, (list, tuple)):
            augmented_point = np.array([points[0], points[1], points[2], 1])
            transformed = np.dot(self.affine, augmented_point)
            return transformed[0], transformed[1], transformed[2]
        elif isinstance(points, np.ndarray):
            assert points.shape[1] == 3, "Input array should be of shape N x 3"
            augmented_points = np.hstack([points, np.ones((points.shape[0], 1))])
            transformed = np.dot(augmented_points, self.affine.T)
            return transformed[:, :3]
        else:
            raise ValueError(
                "Input should be a tuple/list or a numpy array of shape (N, 3)."
            )

    def set_translation(self, dx, dy, dz):
        """Set the translation part of the affine transform."""
        self.affine[0, 3] = dx
        self.affine[1, 3] = dy
        self.affine[2, 3] = dz

    def set_rotation(self, rotation_matrix):
        """
        Sets the rotation part of the affine transform.
        :param rotation_matrix: a 3x3 numpy array representing the rotation.
        """
        assert rotation_matrix.shape == (
            3,
            3,
        ), "Rotation matrix should be of shape (3, 3)"
        self.affine[:3, :3] = rotation_matrix

    def from_proto(self, pb: Union[proto.Transform, bytes]):
        """Initialize the Transform object from a Protocol Buffers message.

        Parameters
        ----------
        pb : Union[proto.Transform, bytes]
            The Protocol Buffers message or its serialized bytes representation.
        """
        if isinstance(pb, bytes):
            pb = proto.Transform.FromString(pb)
        self.srs = pb.srs
        self.affine = np.array(pb.affine).reshape((4, 4))

    def to_proto(self) -> proto.City:
        """Convert the Transform object to a Protocol Buffers message.

        Returns
        -------
        proto.Transform
            A Protocol Buffers message representing the Transform object.
        """
        pb = proto.Transform()
        pb.srs = self.srs
        pb.affine.extend(self.affine.flatten())
        return pb
