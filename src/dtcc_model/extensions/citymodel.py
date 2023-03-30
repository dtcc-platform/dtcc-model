# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import dtcc_model

from dtcc_model.logging import *


def __str__(self):
    return f'DTCC CityModel with {len(self.buildings)} building(s)'


def add_building(self, building):
    'Add a building to the city model'
    self.buildings.append(building)
    info(f'Added building with UUID {building.uuid} to city model')


def remove_building(self, building):
    'Remove a building from the city model. The argument can be a building or a UUID.'

    # Get UUID
    if isinstance(building, str):
        uuid = building
    elif isinstance(building, dtcc_model.Building):
        uuid = building.uuid
    else:
        raise RuntimeError(
            'Unable to remove building; argument must be a building or a UUID')

    # Find matching indices
    indices = [i for i, b in enumerate(self.buildings) if b.uuid == uuid]

    # Remove buildings
    offset = 0
    for index in indices:
        del self.buildings[index + offset]
        offset -= 1
    info(
        f'Removed {len(indices)} building(s) with UUID {uuid} from city model')


dtcc_model.CityModel.__str__ = __str__
dtcc_model.CityModel.add_building = add_building
dtcc_model.CityModel.remove_building = remove_building
