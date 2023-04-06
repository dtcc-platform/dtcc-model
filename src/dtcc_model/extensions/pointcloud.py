# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import dtcc_model

from dtcc_model.logging import info


def __str__(self):
    return f'DTCC PointCloud with {len(self.points)} point(s)'


def add_point(self, point):
    'Add a point to the point cloud'
    self.points.append(point)
    info(f'Added point to point cloud')


dtcc_model.PointCloud.__str__ = __str__
dtcc_model.PointCloud.add_point = add_point
