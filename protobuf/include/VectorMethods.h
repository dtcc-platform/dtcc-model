#include <cmath>

#include "protobuf/dtcc.pb.h"

namespace DTCC
{
  /// Addition of vectors (3D)
  Vector3D operator+ (const Vector3D& v, const Vector3D& w)
  {
    Vector3D u{};
    u.set_x(v.x() + w.x());
    u.set_y(v.y() + w.y());
    u.set_z(v.z() + w.z());
    return u;
  }

  Vector3D operator+ (const Vector3D& v, const double& d)
  {
    Vector3D u{};
    u.set_x(v.x() + d);
    u.set_y(v.y() + d);
    u.set_z(v.z() + d);
    return u;
  }

  /// Subtraction of vectors (3D)
  Vector3D operator- (const Vector3D& v, const Vector3D& w)
  {
    Vector3D u{};
    u.set_x(v.x() - w.x());
    u.set_y(v.y() - w.y());
    u.set_z(v.z() - w.z());
    return u;
  }

  Vector3D operator- (const Vector3D& v, const double& d)
  {
    Vector3D u{};
    u.set_x(v.x() - d);
    u.set_y(v.y() - d);
    u.set_z(v.z() - d);
    return u;
  }

  Vector3D operator* (const Vector3D& v, const double& s)
  {
    Vector3D u{};
    u.set_x(v.x() * s);
    u.set_y(v.y() * s);
    u.set_z(v.z() * s);
    return u;
  }


  double SquaredMagnitude(const Vector3D& v)
  {
    return v.x() * v.x() + v.y() * v.y() + v.z() * v.z();
  }

  double Magnitude(const Vector3D& v)
  {
    return std::sqrt(SquaredMagnitude(v));
  }

  double Dot(const Vector3D& v, const Vector3D& w)
  {
    return v.x() * w.x() + v.y() * w.y() + v.z() * w.z();
  }

  Vector3D Cross(const Vector3D& v, const Vector3D& w)
  {
    Vector3D u{};
    u.set_x(v.y() * w.z() - v.z() * w.y());
    u.set_y(v.z() * w.x() - v.x() * w.z());
    u.set_z(v.x() * w.y() - v.y() * w.x());
    return u;
  }  
  
}