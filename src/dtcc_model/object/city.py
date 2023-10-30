# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

from dataclasses import dataclass

from .object import Object
from dtcc_model import dtcc_pb2 as proto


@dataclass
class NewCity(Object):
    """Represents a city, the top-level container class for city models."""

    pass
