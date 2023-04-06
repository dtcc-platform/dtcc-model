# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import dtcc_model


def __str__(self):
    return f'DTCC VolumeMesh with {len(self.vertices)} vertices, {len(self.cells)} cell(s), and {len(self.markers)} marker(s)'


dtcc_model.VolumeMesh.__str__ = __str__
