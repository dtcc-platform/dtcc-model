# Copyright(C) 2024 Dag Wästberg
# Licensed under the MIT License

from dataclasses import dataclass
from typing import Union

from .object import Object
from dtcc_model import dtcc_pb2 as proto


@dataclass
class Terrain(Object):
    """Represents a terrain object in a city."""

    def to_proto(self) -> proto.Object:
        """Return a protobuf representation of the Terrain.

        Returns
        -------
        proto.Object
            A protobuf representation of the Terrain as an Object.
        """

        # Handle Object fields
        pb = Object.to_proto(self)

        # Set specific fields (currently none)
        _pb = proto.Terrain()
        pb.city.CopyFrom(_pb)

        return pb

    def from_proto(self, pb: Union[proto.Object, bytes]):
        """Initialize Terrain from a protobuf representation.

        Parameters
        ----------
        pb: Union[proto.Object, bytes]
            The protobuf message or its serialized bytes representation.
        """

        # Handle byte representation
        if isinstance(pb, bytes):
            pb = proto.Object.FromString(pb)

        # Handle Object fields
        Object.from_proto(self, pb)

        # Handle specific fields (currently none)
        pass

    def __str__(self):
        out_str = "Terrain object"
        if self.mesh is not None:
            out_str += f" with mesh {self.mesh}"
        if self.raster is not None:
            out_str += f" with raster {self.raster}"
        return out_str
