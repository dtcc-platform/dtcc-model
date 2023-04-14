from shapely.geometry import Polygon


def pb_footprint_to_shapely(pb_footprint):
    shell = []
    holes = []
    for vert in pb_footprint.shell.vertices:
        shell.append((vert.x, vert.y))
    for h in pb_footprint.holes:
        hole = []
        for vert in h.vertices:
            hole.append((vert.x, vert.y))
        if len(hole) > 0:
            holes.append(hole)
    poly = Polygon(shell, holes=holes)
    return poly
