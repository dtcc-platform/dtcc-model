from . import dtcc_pb2 as proto

# Import submodules
from . import object
from . import geometry
from . import quantity

# Import all classes from submodules
from .object import *
from .geometry import *
from .quantity import *


# Collect __all__ from submodules
modules = [object, geometry, quantity]
__all__ = []
for module in modules:
    for name in module.__all__:
        globals()[name] = getattr(module, name)
    __all__ += module.__all__

# FIXME: Old stuff below, remove when stuff is correctly moved into submodules

# from .building import Building
# from .city import City
# from .landuse import Landuse
# from .roadnetwork import RoadNetwork, RoadType

__all__ += [
    "proto",
    "Building",
    "City",
]
