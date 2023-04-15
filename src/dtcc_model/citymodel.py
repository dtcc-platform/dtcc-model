from dataclasses import dataclass, field
import numpy as np
from .building import Building
from typing import Union, tuple


@dataclass
class CityModel:
    buildings: list[Building] = field(default_factory=list)
    terrain: np.ndarray = np.empty((0, 2), dtype=np.float64)  # Height grid or Mesh?
    crs: str = ""
    origin: tuple([float, float]) = (0, 0)
    bounds: tuple([float, float, float, float]) = (0, 0, 0, 0)

    def __str__(self):
        return f"CityModel with {len(self.buildings)} buildings"

    def __len__(self):
        return len(self.buildings)
