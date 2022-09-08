#ifndef DTCC_POINTCLOUD_METHODS_H
#define DTCC_POINTCLOUD_METHODS_H

#include <cmath>
#include <limits>
#include <vector>


#include "protobuf/dtcc.pb.h"
#include "protobuf/include/BoundingBoxMethods.h"
#include "protobuf/include/VectorMethods.h"

namespace DTCC
{
    PointCloud CreatePointCloud(std::vector<Vector3D> pts)
    {
      PointCloud pc;
      google::protobuf::RepeatedPtrField<Vector3D> pt_data(pts.begin(), pts.end());
      pc.mutable_points()->Swap(&pt_data);

      return pc;
    }

    PointCloud CreatePointCloud(std::vector<Vector3D> pts, std::vector<int> classification)
    {
      PointCloud pc = CreatePointCloud(pts);
      google::protobuf::RepeatedField<uint32_t> cls_data(classification.begin(),classification.end());
      pc.mutable_classification()->Swap(&cls_data);

      return pc;
    }

    void CalculatePointCloudBoundingBox(PointCloud &pc)
    {
      float x,y,z;
      float x_min, x_max, y_min, y_max, z_min, z_max;
      x_min = y_min = z_min = std::numeric_limits<float>::max();
      x_max = y_max = z_max = std::numeric_limits<float>::min();

      size_t pt_count = pc.points_size();
      for (size_t i = 0; i < pt_count; i++)
      {
        x = pc.points(i).x();
        x_min = x<x_min ? x : x_min;
        x_max = x>x_max ? x : x_max;

        y = pc.points(i).y();
        y_min = y<y_min ? y : y_min;
        y_max = y>y_max ? y : y_max;
      }
      BoundingBox2D bb = BoundingBox(x_min, y_min, x_max, y_max);
      pc.mutable_bounds()->Swap(&bb);
    }
}

#endif