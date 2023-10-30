from . import dtcc_pb2 as proto

from .object import *
from .geometry import *

from .gridfield import GridField, GridVectorField
from .meshfield import (
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

from . import object
from . import geometry

# Collect __all__ from submodules
modules = [object, geometry]
__all__ = []
for module in modules:
    for name in module.__all__:
        globals()[name] = getattr(module, name)
    __all__ += module.__all__

# FIXME
__all__ += [
    "proto",
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
