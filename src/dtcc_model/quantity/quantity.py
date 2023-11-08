# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import numpy as np
from dataclasses import dataclass, field

from dtcc_model.model import Model


@dataclass
class Quantity(Model):
    """Represents a physical quantity on a geometry.

    A quantity has a value and a unit of measurement and can represent e.g. physical properties such as a temperature or a velocity vector field.
    The quantity takes a value on each element of a geometry and the value
    may be either scalar or vector-valued.

    A quantity is defined in relation to a specific geometry of an object.
    The geometry is identified by its local name (key) as part of the object.

    Note: Consider extending this class to support tensor-valued quantities.

    Note: Consider making this into a base class and deriving scalar and vector
    quantities from it. For now we just have a single class for both.

    Attributes
    ----------
    name: str
        Name of the quantity.
    value: np.ndarray
        An array of values (scalar or vector-valued) of the quantity.
        The dimension is n x d, where n is the number of elements in the geometry and d is the dimension of the quantity.
    unit: str
        Unit of measurement of the quantity.
    geometry: str
        Name (key) of the geometry on which the quantity is defined.
    """

    name: str = ""
    value: np.ndarray = field(default_factory=lambda: np.empty(0))
    unit: str = ""
    geometry: str = ""

    @property
    def shape(self):
        """Return the value shape of the quantity."""
        return self.value.shape[1]
