# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import dtcc_model


def __str__(self):
    return f'DTCC Building with uuid = {self.uuid}, height = {self.height}'


dtcc_model.Building.__str__ = __str__
