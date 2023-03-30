# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import dtcc_model


def __str__(self):
    return f'DTCC Vector2D with x = {self.x}, y = {self.y}'


dtcc_model.Vector2D.__str__ = __str__
