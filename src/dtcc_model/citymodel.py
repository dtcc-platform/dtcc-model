from dataclasses import dataclass
import numpy as np
from .building import Building


@dataclass
class CityModel:
    buildings: list[Building]
    terrain: np.ndarray  # Height grid or Mesh?
    crs: str
    origin: tuple(float, float)
    bounds: tuple(float, float, float, float)

    def __str__(self):
        return f"CityModel with {len(self.buildings)} buildings"
