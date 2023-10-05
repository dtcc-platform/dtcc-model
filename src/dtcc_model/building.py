# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

import numpy as np
from shapely.geometry import Polygon
from typing import Any, Union
from dataclasses import dataclass, field

from .model import DTCCModel
from . import dtcc_pb2 as proto
from .pointcloud import PointCloud
from .meshes import Mesh
from .utils import pb_polygon_to_shapely, pb_polygon_from_shapely


@dataclass
class Building(DTCCModel):
    """A base representation of a single building.

    Parameters
    ----------
    uuid : str, optional
        The UUID of the building, by default "NONE".
    footprint : Polygon, optional
        The polygon representing the footprint of the building, by default an empty Polygon.
    height : float, optional
        The height of the building, by default 0.
    ground_level : float, optional
        The ground level of the base of the building, by default 0.
    roofpoints : PointCloud, optional
        The point cloud representing the roof points of the building, by default an empty PointCloud.
    crs : str, optional
        The coordinate reference system of the building, by default "".
    error : int, optional
        Encoding the errors that occurred when generating a 3D representation of the building, by default 0.
    properties : dict, optional
        Additional properties of the building, by default an empty dict.

    """

    uuid: str = "NONE"
    footprint: Polygon = Polygon()
    height: float = 0
    ground_level: float = 0
    floors: int = 1
    roofpoints: PointCloud = field(default_factory=PointCloud)
    crs: str = ""
    error: int = 0
    mesh: Mesh = field(default_factory=Mesh)
    properties: dict = field(default_factory=dict)

    def __str__(self):
        """Provide a human-readable representation of the building.

        Returns
        -------
        str
            A string representation of the building with its UUID and footprint area.

        """
        return f"DTCC Building {self.uuid} with {self.footprint.area} m² footprint"

    @property
    def area(self):
        """Calculate the area of the building's footprint.

        Returns
        -------
        float
            Area of the footprint.

        """
        return self.footprint.area

    def from_proto(self, pb: Union[proto.Building, bytes]):
        """Update the building attributes from a protobuf representation.

        Parameters
        ----------
        pb : Union[proto.Building, bytes]
            Protobuf representation of a building or its byte string.

        """
        if isinstance(pb, bytes):
            pb = proto.Building.FromString(pb)
        self.footprint = pb_polygon_to_shapely(pb.footprint)
        self.uuid = pb.uuid
        self.height = pb.height
        self.ground_level = pb.groundHeight
        self.error = pb.error
        self.roofpoints = PointCloud()
        self.roofpoints.points = np.array(pb.roofpoints.points).reshape(-1, 3)

    def to_proto(self) -> proto.Building:
        """Convert the building attributes to a protobuf representation.

        Returns
        -------
        proto.Building
            Protobuf representation of the building.

        """
        pb = proto.Building()
        pb.uuid = self.uuid
        pb.height = self.height
        pb.groundHeight = self.ground_level
        pb.error = self.error
        pb.footprint.CopyFrom(pb_polygon_from_shapely(self.footprint))
        pb.roofpoints.points.extend(self.roofpoints.points.flatten())
        return pb

    def __getitem__(self, key: str) -> Any:
        """Retrieve property values using dictionary-like access.

        Parameters
        ----------
        key : str
            Name of the property.

        Returns
        -------
        Any
            Value of the property.

        Raises
        ------
        KeyError
            If the property is not found.

        """
        # handle special properties
        if key == "height":
            return self.height
        elif key == "ground_level":
            return self.ground_level
        elif key == "uuid":
            return self.uuid
        elif key == "error":
            return self.error
        # handle generic properties
        elif key in self.properties:
            return self.properties[key]
        else:
            raise KeyError(f"Property {key} not found")

    def __setitem__(self, key: str, value: Any):
        """Set property values using dictionary-like access.

        Parameters
        ----------
        key : str
            Name of the property.
        value : Any
            Value to set for the property.

        """
        # handle special properties
        if key == "height":
            self.height = value
        elif key == "ground_level":
            self.ground_level = value
        elif key == "uuid":
            self.uuid = value
        elif key == "error":
            self.error = value
        # handle generic properties
        else:
            self.properties[key] = value
