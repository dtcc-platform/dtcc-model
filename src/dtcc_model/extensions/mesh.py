# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import dtcc_model

from dtcc_model.logging import info


def __str__(self):
    return f'DTCC Mesh with {len(self.vertices)} vertices, {len(self.normals)} normal(s), and {len(self.faces)} face(s)'


def add_vertex(self, vertex):
    'Add a vertex (Vector3D) to the mesh'
    self.vertices.append(vertex)
    info(f'Added vertex to mesh')


def add_face(self, face):
    'Add a face (Triangle) to the mesh'
    self.faces.append(face)
    info(f'Added face to mesh')


dtcc_model.Mesh.__str__ = __str__
dtcc_model.Mesh.add_vertex = add_vertex
dtcc_model.Mesh.add_face = add_face
