# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import dtcc_model


def __str__(self):
    return f'DTCC Vector3D with x = {self.x}, y = {self.y}, z = {self.z}'


dtcc_model.Vector3D.__str__ = __str__
