#ifndef DTCC_GRID_METHODS_H
#define DTCC_GRID_METHODS_H


#include "protobuf/dtcc.pb.h"
#include "protobuf/include/VectorMethods.h"
#include "Utils.h"

namespace DTCC
{
  Grid2D Grid(BoundingBox2D bbox, size_t xSize, size_t ySize)
  {
    assert(xSize > 1);
    assert(ySize > 1);

    Grid2D grid;
    float xSteps = (bbox.q().x()-bbox.p().x()) / static_cast<float>(xSize - 1);
    float ySteps = (bbox.q().y()-bbox.p().y()) / static_cast<float>(ySize - 1);

    grid.mutable_boundingbox()->Swap(&bbox);   
    grid.set_xsize(xSize);
    grid.set_ysize(ySize);
    grid.set_xstep(xSteps);
    grid.set_ystep(ySteps);

    return grid;
  }

  size_t NumVertices(const Grid2D &grid)
  {
    return grid.xsize()*grid.ysize();
  }

  size_t NumCells(const Grid2D &grid)
  {
    if (grid.xsize() == 0 || grid.ysize() == 0)
      return 0;
    return (grid.xsize() - 1)*(grid.ysize() - 1);
  }

  /// Map point to index of closest vertex.
  ///
  /// @param grid Grid2D
  /// @param p Point
  /// @return Vertex index
  size_t Point2Index(const Grid2D &grid,const Vector2D &p)
  {
    const double _x = p.x() - grid.boundingbox().p().x();
    const double _y = p.y() - grid.boundingbox().p().y();
    const long int ix = Utils::crop(std::lround(_x / grid.xstep()), grid.xsize());
    const long int iy = Utils::crop(std::lround(_y / grid.ystep()), grid.ysize());
    return ix + iy * grid.xsize();
  }

  /// Map vertex index to point.
  ///
  /// @param grid Grid2D
  /// @param i Vertex index
  /// @return Vertex coordinates as a point
  Vector2D Index2Point(const Grid2D &grid, size_t i)
  {
    const size_t ix = i % grid.xsize();
    const size_t iy = i / grid.xsize();
    return Vector(grid.boundingbox().p().x() + ix * grid.xstep(),
                    grid.boundingbox().p().y() + iy * grid.ystep());
  }
}
#endif