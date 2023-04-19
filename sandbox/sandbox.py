# Playground for testing

from dtcc_model import *

from numpy import array

v = array([[0, 0, 0], [1, 0, 0], [0, 1, 0]], dtype=float)
n = array([[0, 0, 1]], dtype=float)
t = array([[0, 1, 2]])

mesh = Mesh()

mesh = Mesh(v, n, t)
proto_mesh = mesh.to_proto()
mesh.from_proto(proto_mesh)
print(mesh)

v = array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float)
t = array([[0, 1, 2, 3]])

volume_mesh = VolumeMesh(v, t)
proto_volume_mesh = volume_mesh.to_proto()
volume_mesh.from_proto(proto_volume_mesh)
print(volume_mesh)

building = Building()
city_model = CityModel()
city_model.add_building(building)
print(building)
print(city_model)


# print(dir(mesh))

# print(mesh)
# print(proto_mesh)

# from dtcc_model import *
# from dtcc_model.logging import *

# set_log_level(logging.DEBUG)

# mesh = Mesh()

# x2 = Vector3D()
# x3 = Vector3D()
# triangle = Triangle()
# pointcloud = PointCloud()
# mesh = Mesh()
# building = Building()
# citymodel = CityModel()

# x2.x = 3.0
# x2.y = 5.0

# triangle.v0 = 0
# triangle.v1 = 1
# triangle.v2 = 2

# pointcloud.add_point(x3)
# pointcloud.add_point(x3)
# pointcloud.add_point(x3)

# mesh.add_vertex(x3)
# mesh.add_vertex(x3)
# mesh.add_vertex(x3)
# mesh.add_face(triangle)

# building.uuid = 'da39f9a4-2ae1-402b-8b00-897b11e37c05'
# building.height = 250.0
# citymodel.add_building(building)
# citymodel.add_building(building)

# info(x2)
# info(x3)
# info(pointcloud)
# info(mesh)
# info(building)
# info(citymodel)

# citymodel.remove_building(building)
