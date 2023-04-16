#ifndef DTCC_POINTCLOUD_METHODS_H
#define DTCC_POINTCLOUD_METHODS_H

#include <cmath>
#include <limits>
#include <vector>

#include "dtcc.pb.h"
#include "BoundingBoxMethods.h"
#include "VectorMethods.h"

namespace DTCC
{
  /// Create points
  Vector2D Point(float x, float y)
  {
    Vector2D v;
    v.set_x(x);
    v.set_y(y);
    return v;
  }

  Vector3D Point(float x, float y, float z)
  {
    Vector3D v;
    v.set_x(x);
    v.set_y(y);
    v.set_z(z);
    return v;
  }

  PointCloud CreatePointCloud(const std::vector<float> pts)
  {
    PointCloud pc;
    google::protobuf::RepeatedField<float> pts_data(pts.begin(), pts.end());
    pc.mutable_points()->Swap(&pts_data);
    return pc;
  }

  PointCloud CreatePointCloud(const std::vector<Vector3D> pts)
  {
    PointCloud pc;
    std::vector<float> flat_points;
    for (auto &pt : pts)
    {
      flat_points.push_back(pt.x());
      flat_points.push_back(pt.y());
      flat_points.push_back(pt.z());
    }
    return CreatePointCloud(flat_points);
    return pc;
  }

  PointCloud CreatePointCloud(const std::vector<float> pts, const std::vector<int> classification)
  {
    PointCloud pc = CreatePointCloud(pts);
    google::protobuf::RepeatedField<uint32_t> cls_data(classification.begin(), classification.end());
    pc.mutable_classification()->Swap(&cls_data);

    return pc;
  }

  PointCloud CreatePointCloud(const std::vector<Vector3D> pts, const std::vector<int> classification)
  {
    PointCloud pc = CreatePointCloud(pts);
    google::protobuf::RepeatedField<uint32_t> cls_data(classification.begin(), classification.end());
    pc.mutable_classification()->Swap(&cls_data);

    return pc;
  }

  PointCloud CreatePointCloud(std::vector<float> pts, std::vector<int> classification,
                              std::vector<int> intensity)
  {
    PointCloud pc = CreatePointCloud(pts);
    google::protobuf::RepeatedField<uint32_t> cls_data(classification.begin(), classification.end());
    pc.mutable_classification()->Swap(&cls_data);

    google::protobuf::RepeatedField<uint32_t> intensity_data(intensity.begin(), intensity.end());
    pc.mutable_intensity()->Swap(&intensity_data);

    return pc;
  }

  PointCloud CreatePointCloud(std::vector<float> pts, std::vector<int> classification,
                              std::vector<int> intensity, std::vector<int> return_number, std::vector<int> num_return)
  {
    PointCloud pc = CreatePointCloud(pts);
    google::protobuf::RepeatedField<uint32_t> cls_data(classification.begin(), classification.end());
    pc.mutable_classification()->Swap(&cls_data);

    google::protobuf::RepeatedField<uint32_t> intensity_data(intensity.begin(), intensity.end());
    pc.mutable_intensity()->Swap(&intensity_data);

    google::protobuf::RepeatedField<uint32_t> retnum_data(return_number.begin(), return_number.end());
    pc.mutable_intensity()->Swap(&retnum_data);

    google::protobuf::RepeatedField<uint32_t> numret_data(num_return.begin(), num_return.end());
    pc.mutable_intensity()->Swap(&numret_data);

    return pc;
  }

}

#endif