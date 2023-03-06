#ifndef DTCC_POLYGON_METHODS_H
#define DTCC_POLYGON_METHODS_H

#include <cmath>
#include <vector>

#include "dtcc_model/dtcc.pb.h"

namespace DTCC
{

  Vector2D Vertex(double x , double y) 
  {
    Vector2D v;
    v.set_x(x);
    v.set_y(y);
    return v;
  }

  Vector3D Vertex(double x, double y, double z)
  {
    Vector3D v;
    v.set_x(x);
    v.set_y(y);
    v.set_z(z);
    return v;
  }

  LinearRing CreateLinearRing(const std::vector<Vector2D> &verts)
  {
    LinearRing linearRing;
    for (const auto &v: verts)
    {
      auto ring_vert = linearRing.add_vertices();
      ring_vert->set_x(v.x());
      ring_vert->set_y(v.y());
    }
    return linearRing;
  }

  Polygon CreatePolygon(const std::vector<Vector2D> &verts)
  {
    Polygon p;
    LinearRing *shell = new LinearRing; // = CreateLinearRing(verts);
    
    shell->CopyFrom(CreateLinearRing(verts));
    p.set_allocated_shell(shell);
    return p;
  }

  Polygon CreatePolygon(const std::vector<Vector2D> &verts, const std::vector<LinearRing> &holes)
  {
    Polygon p = CreatePolygon(verts);
    size_t num_holes = holes.size();
    for (size_t i = 0; i<num_holes; i++)
    {
      auto polygon_hole = p.add_holes();
      polygon_hole->CopyFrom(holes[i]);
    }
    return p;
  }

  Polygon CreatePolygon(const std::vector<Vector2D> &verts, const std::vector<std::vector<Vector2D>> &holes)
  {
    std::vector<LinearRing> lr_holes;
    for (const auto &vert_list: holes )
    {
      lr_holes.push_back(CreateLinearRing(vert_list));
    }
    return CreatePolygon(verts,lr_holes);

  }

  Polygon CreatePolygon(const std::vector<std::vector<float_t>> &vertices)
  {
    std::vector<Vector2D> vert_vector;
    for(const auto &v: vertices)
    {
      vert_vector.push_back( Vertex(v[0],v[1]));
    }
    return CreatePolygon(vert_vector);
  }

  Polygon CreatePolygon(const std::vector<std::vector<float_t>> &vertices, const std::vector<std::vector<std::vector<float_t>>> &holes )
  {
    std::vector<Vector2D> vert_vector;
    std::vector<std::vector<Vector2D>> holes_vector;
    for(const auto &v: vertices)
    {
      vert_vector.push_back( Vertex(v[0],v[1]));
    }

    for (const auto hole: holes)
    {
      std::vector<Vector2D> hole_vec;
      for (const auto &v: hole)
      {
        hole_vec.push_back( Vertex(v[0],v[1]));
      }
      holes_vector.push_back(hole_vec);
    }
    return CreatePolygon(vert_vector, holes_vector);
  }

  void AddVertex(Polygon &p, const Vector2D &v)
  {
    p.mutable_shell()->add_vertices()->CopyFrom(v);
  }

  void ClosePolygon(LinearRing &p)
  {
    
  }

  void ClosePolygon(Polygon &p)
  {

  }

  void OffsetPolygon(Polygon &p, const Vector2D &O)
  {
    float o_x = O.x();
    float o_y = O.y();
    auto shell = p.mutable_shell();
    for (size_t i = 0; i<shell->vertices_size(); i++)
    {

      float x = shell->vertices()[i].x();
      float y = shell->vertices()[i].y();
      auto vertex = shell->mutable_vertices(i);
      vertex->set_x(x+o_x); 
      vertex->set_y(y+o_y); 
    }
  }

}

#endif
