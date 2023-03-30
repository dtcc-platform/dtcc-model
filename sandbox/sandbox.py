# Playground for testing

from dtcc_model import *
from dtcc_model.logging import *

set_log_level(logging.DEBUG)

x2 = Vector3D()
x3 = Vector3D()
pointcloud = PointCloud()
building = Building()
citymodel = CityModel()

x2.x = 3.0
x2.y = 5.0

pointcloud.add_point(x3)
pointcloud.add_point(x3)
pointcloud.add_point(x3)

building.uuid = 'da39f9a4-2ae1-402b-8b00-897b11e37c05'
building.height = 250.0
citymodel.add_building(building)
citymodel.add_building(building)

info(x2)
info(x3)
info(pointcloud)
info(building)
info(citymodel)

citymodel.remove_building(building)
