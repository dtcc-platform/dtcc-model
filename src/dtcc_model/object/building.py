# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

from dataclasses import dataclass, field
from shapely.geometry import Polygon

from .object import Object
from dtcc_model.geometry import Bounds
from dtcc_model.object import GeometryType
from dtcc_model import dtcc_pb2 as proto


@dataclass
class Building(Object):
    """Represents a building in a city."""

    @property
    def building_parts(self):
        """Return list of building parts in building."""
        return self.children[BuildingPart] if BuildingPart in self.children else []

    @property
    def height(self):
        self.bounds.zmax

    def to_proto(self):
        """Return a protobuf representation of the Building.

        Returns
        -------
        proto.Object
            A protobuf representation of the Building and as an Object.
        """

        # Handle Object fields
        pb = Object.to_proto(self)

        # Handle specific fields (currently none)
        _building = proto.Building()
        pb.building.CopyFrom(_building)

        return pb

    def from_proto(self, pb):
        """Initialize Building from a protobuf representation.

        Parameters
        ----------
        pb: Union[proto.Object, bytes]
            The protobuf message or its serialized bytes representation.
        """

        # Handle Object fields
        Object.from_proto(self, pb)

        # Handle specific fields (currently none)
        pass


class BuildingPart(Object):
    # TODO: Implement to_proto and from_proto
    def to_proto(self):
        pass

    def from_proto(self, pb):
        pass
