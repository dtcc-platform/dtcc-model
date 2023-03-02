#ifndef DTCC_BOUNDINGBOX_METHODS_H
#define DTCC_BOUNDINGBOX_METHODS_H

#include <cmath>

#include "protobuf/dtcc.pb.h"

namespace DTCC
{

  BoundingBox2D BoundingBox(float min_x, float min_y, float max_x, float max_y)
  {
    BoundingBox2D bb;
    bb.mutable_p()->set_x(min_x);
    bb.mutable_p()->set_y(min_y);
    bb.mutable_q()->set_x(max_x);
    bb.mutable_q()->set_y(max_y);

    return bb;
  }

  BoundingBox2D BoundingBox(const Vector2D &P, const Vector2D &Q)
  {
    return BoundingBox(P.x(), P.y(), Q.x(),Q.y());
  }

  BoundingBox2D BoundingBox(const Polygon &p)
  {
    auto shell = p.shell();
    constexpr float max = std::numeric_limits<float>::max();
    float P_x = max;
    float P_y = max;
    float Q_x = -max;
    float Q_y = -max;    

    for (const auto &p : shell.vertices())
    {
      P_x = std::min(P_x, p.x());
      P_y = std::min(P_y, p.y());
      Q_x = std::max(Q_x, p.x());
      Q_y = std::max(Q_y, p.y());
    }

    auto bb = BoundingBox(P_x,P_y,Q_x,Q_y);
    
    return bb;
  }

  

  BoundingBox2D VectorBoundingBox(const std::vector<Vector2D> &vecs)
  {
      
    constexpr float max = std::numeric_limits<float>::max();
    float P_x = max;
    float P_y = max;
    float Q_x = -max;
    float Q_y = -max;    

    for (const auto &p : vecs)
    {
      P_x = std::min(P_x, p.x());
      P_y = std::min(P_y, p.y());
      Q_x = std::max(Q_x, p.x());
      Q_y = std::max(Q_y, p.y());
    }

    auto bb = BoundingBox(P_x,P_y,Q_x,Q_y);
    
    return bb;
  }

  void Buffer(BoundingBox2D &bb, float margin)
  {
    auto p = bb.mutable_p();
    auto q = bb.mutable_q();
    p->set_x(p->x()-margin);
    p->set_y(p->y()-margin);

    q->set_x(q->x()+margin);
    q->set_y(q->y()+margin);
  }

  BoundingBox2D Union(const BoundingBox2D &u,const BoundingBox2D &v)
  {

    float P_x = std::min(u.p().x(), v.p().x());
    float P_y = std::min(u.p().y(), v.p().y());
    float Q_x = std::max(u.q().x(), v.q().x());
    float Q_y = std::max(u.q().y(), v.q().y());

    return BoundingBox(P_x,P_y,Q_x,Q_y);
  }

  double Area(const BoundingBox2D &bb)
  {
    return (bb.q().x()-bb.p().x()) * (bb.q().y()-bb.p().y());
  }
  
  bool BoundingBoxContains2D(const BoundingBox2D &bbox,
                                    const Vector2D &p,
                                    double margin = 0.0)
  {
    return (bbox.p().x() + margin <= p.x() && p.x() + margin <= bbox.q().x() &&
             bbox.p().y() + margin <= p.y() && p.y() + margin <= bbox.q().y());
  }

}
#endif