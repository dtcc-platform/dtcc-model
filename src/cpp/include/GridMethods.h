#ifndef DTCC_GRID_METHODS_H
#define DTCC_GRID_METHODS_H

#include "dtcc_model/dtcc.pb.h"
#include "dtcc_model/BoundingBoxMethods.h"
#include "dtcc_model/VectorMethods.h"

namespace DTCC
{
  /// Crop integer x to interval [0, n - k). Requires care
  /// due to involving both signed and unsigned integers.
  ///
  /// @param x Signed integer
  /// @param n Unsigned integer (length of array)
  /// @param k Unsigned integer (maring at end of array)
  /// @return Unsigned integer within specified range
  size_t crop(long int x, size_t n, size_t k = 0)
  {
    assert(n > 0);
    assert(k < n);
    return x < 0 ? 0 : (x + k >= n ? n - 1 - k : x);
  }
  
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
    const long int ix = crop(std::lround(_x / grid.xstep()), grid.xsize());
    const long int iy = crop(std::lround(_y / grid.ystep()), grid.ysize());
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

  /// Map point to cell and local coordinates.
  ///
  /// @param grid Grid2D
  /// @param p Point
  /// @param i Index of cell containing point
  /// @param x Local X-coordinate on cell (scaled)
  /// @param y Local Y-coordinate on cell (scaled)
  void Point2Cell(const Grid2D &grid, const Vector2D &p,size_t& i, double& x, double& y)
  {
    auto bbox = grid.boundingbox();
    if (!BoundingBoxContains2D(bbox, p)) 
      Error("Point p = " + p.DebugString() + " is outside of domain = " + bbox.DebugString());
    
    double XStep = grid.xstep();
    double YStep = grid.ystep();

    const double _x = p.x() - bbox.p().x();
    const double _y = p.y() - bbox.p().y();
    const size_t ix = crop(std::lround(_x / XStep - 0.5), grid.xsize(), 1);
    const size_t iy = crop(std::lround(_y / YStep - 0.5), grid.ysize(), 1);
    i =  ix + iy * grid.xsize();

    x = (_x - ix*XStep) / XStep;
    y = (_y - iy*YStep) / YStep;

    if (x <= 0.0)
      x = 0.0;
    if (x >= 1.0)
      x = 1.0;
    if (y <= 0.0)
      y = 0.0;
    if (y >= 1.0)
      y = 1.0;
  }

  
}
#endif