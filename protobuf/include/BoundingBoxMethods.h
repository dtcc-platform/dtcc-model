#include <cmath>

#include "protobuf/dtcc.pb.h"

namespace DTCC
{
    BoundingBox2D VectorBoundingBox(const std::vector<Vector2D> &vecs,
                           float margin = 0.0)
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
      P_x -= margin;
      P_y -= margin;
      Q_x += margin;
      Q_y += margin;

      BoundingBox2D bb;

      bb.mutable_p()->set_x(P_x);
      bb.mutable_p()->set_y(P_y);
      bb.mutable_q()->set_x(Q_x);
      bb.mutable_q()->set_y(Q_y);


      return bb;
    }
}