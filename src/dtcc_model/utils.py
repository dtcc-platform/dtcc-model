# Copyright(C) 2023 Dag Wästberg
# Licensed under the MIT License

import shapely.geometry
from dtcc_model import dtcc_pb2


def coords_to_pb_linear_ring(coords):
    """
    Convert a list of coordinates to a protobuf LinearRing.

    Parameters
    ----------
    coords : list of tuple
        A list of (x, y) coordinate tuples.

    Returns
    -------
    dtcc_pb2.LinearRing
        A protobuf LinearRing object.

    """
    lr = dtcc_pb2.LinearRing()
    vertices = []
    for c in coords:
        v = dtcc_pb2.Vector2D()
        v.x = c[0]
        v.y = c[1]
        vertices.append(v)
    lr.vertices.extend(vertices)
    return lr


def pb_polygon_to_shapely(pb_polygon: dtcc_pb2.Polygon) -> shapely.geometry.Polygon:
    """
    Convert a protobuf Polygon to a Shapely Polygon.

    Parameters
    ----------
    pb_polygon : dtcc_pb2.Polygon
        A protobuf Polygon object.

    Returns
    -------
    shapely.geometry.Polygon
        A Shapely Polygon object.

    """
    shell = []
    holes = []
    for vert in pb_polygon.shell.vertices:
        shell.append((vert.x, vert.y))
    for h in pb_polygon.holes:
        hole = []
        for vert in h.vertices:
            hole.append((vert.x, vert.y))
        if len(hole) > 0:
            holes.append(hole)
    poly = shapely.geometry.Polygon(shell, holes=holes)
    return poly


def pb_polygon_from_shapely(polygon):
    """
    Convert a Shapely Polygon to a protobuf Polygon.

    Parameters
    ----------
    polygon : shapely.geometry.Polygon
        A Shapely Polygon object.

    Returns
    -------
    dtcc_pb2.Polygon
        A protobuf Polygon object.

    """
    pb_polygon = dtcc_pb2.Polygon()
    shell = polygon.exterior.coords
    shell = coords_to_pb_linear_ring(shell)
    pb_polygon.shell.CopyFrom(shell)
    if len(polygon.interiors) > 0:
        holes = []
        for hole in polygon.interiors:
            hole = coords_to_pb_linear_ring(hole.coords)
            holes.append(hole)
        pb_polygon.holes.extend(holes)
    return pb_polygon
