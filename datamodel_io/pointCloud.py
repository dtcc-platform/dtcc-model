from pathlib import Path
import numpy as np
import laspy
from datamodel_io.pblib.generate_protobuf import PBPointCloud
from dtcc.dtcc_pb2 import PointCloud


def loadLAS(
    lasfiles,
    points_only=False,
    points_classification_only=False,
    return_serialized=True,
):
    if isinstance(lasfiles, str) or isinstance(lasfiles, Path):
        lasfiles = [lasfiles]
    pts = None
    classification = np.array([]).astype(np.uint8)
    intensity = np.array([]).astype(np.uint16)
    returnNumber = np.array([]).astype(np.uint8)
    numberOfReturns = np.array([]).astype(np.uint8)
    for filename in lasfiles:
        las = laspy.read(filename)
        if pts is None:
            pts = las.xyz
        else:
            pts = np.concatenate((pts,las.xyz))

        if not points_only:
            classification = np.concatenate((classification,np.array(las.classification)))
        if not (points_only or points_classification_only):
            intensity = np.concatenate((intensity,np.array(las.intensity)))
            returnNumber = np.concatenate((returnNumber,np.array(las.return_num)))
            numberOfReturns = np.concatenate((numberOfReturns, np.array(las.num_returns)))
        print(classification.shape)
    if pts is not None:
        pb = PBPointCloud(pts, classification, intensity, returnNumber, numberOfReturns)
    else:
        return None

    if return_serialized:
        return pb
    else:
        pc = PointCloud()
        pc.ParseFromString(pb)
        return pc


def writeLAS(pointcloud, las_file):
    pass
    # WIP
    # hdr = laspy.header.Header()
    # outfile = laspy.file.File(las_file,mode='w',header=hdr)
