from dataclasses import dataclass
import numpy as np


@dataclass
class Pointcloud:
    points: np.ndarray
    classification: np.ndarray
    intensity: np.ndarray
    return_number: np.ndarray
    number_of_returns: np.ndarray
    crs: str
    origin: tuple(float, float)
    bounds: tuple(float, float, float, float)

    def __str__(self):
        return f"Pointcloud with {self.points.shape[0]} points"

    def used_classifications(self):
        return np.unique(self.classification)
