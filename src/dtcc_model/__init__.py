from . import dtcc_pb2 as proto

from .geometry import *

from .grid import Grid
from .meshes import Mesh, VolumeMesh
from .gridfields import GridField, GridVectorField
from .meshfields import (
    MeshField,
    MeshVectorField,
    VolumeMeshField,
    VolumeMeshVectorField,
)
from .building import Building
from .city import City
from .raster import Raster
from .landuse import Landuse
from .roadnetwork import RoadNetwork, RoadType


from . import geometry

# Collect __all__ from submodules
modules = [geometry]
__all__ = []
for module in modules:
    for name in module.__all__:
        globals()[name] = getattr(module, name)
    __all__ += module.__all__

# FIXME
__all__ += [
    "proto",
    "Bounds",
    "Georef",
    "PointCloud",
    "Grid",
    "Mesh",
    "VolumeMesh",
    "GridField",
    "GridVectorField",
    "MeshField",
    "MeshVectorField",
    "VolumeMeshField",
    "VolumeMeshVectorField",
    "Building",
    "City",
    "Raster",
    "RoadNetwork",
]
