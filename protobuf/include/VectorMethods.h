
#ifndef DTCC_VECTOR_METHODS_H
#define DTCC_VECTOR_METHODS_H

#include <cmath>

#include "protobuf/dtcc.pb.h"

namespace DTCC
{
  /// Create vector
  Vector2D Vector(float x, float y)
  {
    Vector2D v;
    v.set_x(x);
    v.set_y(y);
    return v;
  }

  Vector3D Vector(float x, float y, float z)
  {
    Vector3D v;
    v.set_x(x);
    v.set_y(y);
    v.set_z(z);
    return v;
  }

  /// Addition of vectors
  Vector2D operator+ (const Vector2D& v, const Vector2D& w)
  {
    Vector2D u{};
    u.set_x(v.x() + w.x());
    u.set_y(v.y() + w.y());
    return u;
  }

  Vector2D operator+ (const Vector2D& v, const double& d)
  {
    Vector2D u{};
    u.set_x(v.x() + d);
    u.set_y(v.y() + d);
    return u;
  }

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

  /// Subtraction of vectors 
  Vector2D operator- (const Vector2D& v, const Vector2D& w)
  {
    Vector2D u{};
    u.set_x(v.x() - w.x());
    u.set_y(v.y() - w.y());
    return u;
  }

  Vector2D operator- (const Vector2D& v, const double& d)
  {
    Vector2D u{};
    u.set_x(v.x() - d);
    u.set_y(v.y() - d);
    return u;
  }

  Vector2D operator- (const Vector2D& v)
  {
    Vector2D u{};
    u.set_x(-v.x());
    u.set_y(-v.y());
    return u;
  }

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

  Vector3D operator- (const Vector3D& v)
  {
    Vector3D u{};
    u.set_x(-v.x());
    u.set_y(-v.y());
    u.set_z(-v.z());
    return u;
  }

  /// Multiplication 
  Vector2D operator* (const Vector2D& v, const double& s)
  {
    Vector2D u{};
    u.set_x(v.x() * s);
    u.set_y(v.y() * s);
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

    /// Division
  Vector2D operator/ (const Vector2D& v, const double& s)
  {
    Vector2D u{};
    u.set_x(v.x() / s);
    u.set_y(v.y() / s);
    return u;
  }

  Vector3D operator/ (const Vector3D& v, const double& s)
  {
    Vector3D u{};
    u.set_x(v.x() / s);
    u.set_y(v.y() / s);
    u.set_z(v.z() / s);
    return u;
  }

  // Magnitude of a vector
  double SquaredMagnitude(const Vector2D& v)
  {
    return v.x() * v.x() + v.y() * v.y();
  }

  double Magnitude(const Vector2D& v)
  {
    return std::sqrt(SquaredMagnitude(v));
  }

  double SquaredMagnitude(const Vector3D& v)
  {
    return v.x() * v.x() + v.y() * v.y() + v.z() * v.z();
  }

  double Magnitude(const Vector3D& v)
  {
    return std::sqrt(SquaredMagnitude(v));
  }

  double Dot(const Vector2D& v, const Vector2D& w)
  {
    return v.x() * w.x() + v.y() * w.y();
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

#endif
