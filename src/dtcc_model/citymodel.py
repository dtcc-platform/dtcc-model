from dataclasses import dataclass, field
import numpy as np
from .building import Building
from typing import Union, Tuple
import dtcc_model.dtcc_pb2 as proto


@dataclass
class CityModel:
    buildings: list[Building] = field(default_factory=list)
    terrain: np.ndarray = np.empty((0, 2), dtype=np.float64)  # Height grid or Mesh?
    crs: str = ""
    origin: Tuple[float, float] = (0, 0)
    bounds: Tuple[float, float, float, float] = (0, 0, 0, 0)

    def __str__(self):
        return f"CityModel with {len(self.buildings)} buildings"

    def __len__(self):
        return len(self.buildings)

    def to_proto(self) -> proto.CityModel:
        proto_citymodel = proto.CityModel()
        proto_citymodel.buildings.extend([b.to_proto() for b in self.buildings])
        proto_citymodel.georeference.crs = self.crs
        proto_citymodel.georeference.x0 = self.origin[0]
        proto_citymodel.georeference.y0 = self.origin[1]
        proto_citymodel.bounds.p.x = self.bounds[0]
        proto_citymodel.bounds.p.y = self.bounds[1]
        proto_citymodel.bounds.q.x = self.bounds[2]
        proto_citymodel.bounds.q.y = self.bounds[3]
        return proto_citymodel

    def from_proto(self, proto_citymodel: Union[proto.CityModel, bytes]):
        if isinstance(proto_citymodel, bytes):
            _citymodel = proto.CityModel()
            _citymodel.ParseFromString(proto_citymodel)
            proto_citymodel = _citymodel
        buildings = []
        for b in proto_citymodel.buildings:
            bld = Building()
            bld.from_proto(b)
            buildings.append(bld)

        self.buildings = buildings

        if proto_citymodel.georeference.crs:
            self.crs = proto_citymodel.georeference.crs
        self.origin = (proto_citymodel.georeference.x0, proto_citymodel.georeference.y0)
        self.bounds = (
            proto_citymodel.bounds.p.x,
            proto_citymodel.bounds.p.y,
            proto_citymodel.bounds.q.x,
            proto_citymodel.bounds.q.y,
        )
