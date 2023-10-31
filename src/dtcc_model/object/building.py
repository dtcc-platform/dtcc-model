# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

from dataclasses import dataclass

from .object import Object
from dtcc_model import dtcc_pb2 as proto


@dataclass
class NewBuilding(Object):
    """Represents a building in a city."""

    pass
