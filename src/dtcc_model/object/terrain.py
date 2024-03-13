# Copyright(C) 2024 Dag Wästberg
# Licensed under the MIT License

from dataclasses import dataclass

from .object import Object
from dtcc_model import dtcc_pb2 as proto


@dataclass
class Terrain(Object):
    """Represents a terrain object in a city."""

    def to_proto(self):
        """Return a protobuf representation of the Terrain.

        Returns
        -------
        proto.Object
            A protobuf representation of the Terrain and as an Object.
        """

        # Handle Object fields
        pb = Object.to_proto(self)

        # Set specific fields (currently none)
        _terrain = proto.Terrain()
        pb.city.CopyFrom(_terrain)

        return pb

    def from_proto(self, pb):
        pass

    # TODO: Implement to_proto and from_proto
    def to_proto(self):
        pass
