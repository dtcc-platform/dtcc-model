import numpy as np
import laspy
from pblib.generate_protobuf import PBPointCloud
from dtcc.dtcc_pb2 import PointCloud

def loadLAS(filename, points_only = False, points_classification_only = False, return_serialized=True):
    las = laspy.read(filename)
    pts = las.xyz
    classification = np.array([]).astype(np.uint8)
    intensity = np.array([]).astype(np.uint16)
    returnNumber = np.array([]).astype(np.uint8)
    numberOfReturns = np.array([]).astype(np.uint8)
    if not points_only:
        classification = np.array(las.classification)
    if not(points_only or points_classification_only):
        intensity = np.array(las.intensity)
        returnNumber = np.array(las.return_num)
        numberOfReturns = np.array(las.num_returns)
    print(classification.shape)
    pb = PBPointCloud(pts, classification, intensity, returnNumber, numberOfReturns)
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
    
