#ifndef DTCC_GRIDFIELD_METHODS_H
#define DTCC_GRIDFIELD_METHODS_H


#include "dtcc_model/dtcc.pb.h"
#include "dtcc_model//BoundingBoxMethods.h"
#include "dtcc_model//VectorMethods.h"
#include "dtcc_model//GridMethods.h"

namespace DTCC
{

  GridField2D GridField(const Grid2D& grid, float initial_val = 0)
  {
    GridField2D gridfield;
    size_t num_verts = NumVertices(grid);
    gridfield.mutable_grid()->CopyFrom(grid);
    gridfield.mutable_values()->Reserve(num_verts);
    for (size_t i = 0; i<num_verts;i++)
    {
      gridfield.add_values(initial_val);
    }
    return gridfield;
  }

  GridField2D GridField(const Grid2D& grid, std::vector<float> initial_vals)
  {
    GridField2D gridfield;
    size_t num_verts = NumVertices(grid);
    assert(initial_vals.size()<num_verts);

    gridfield.mutable_grid()->CopyFrom(grid);
    gridfield.mutable_values()->Reserve(num_verts);
    for (size_t i = 0; i<num_verts;i++)
    {
      gridfield.add_values(initial_vals[i]);
    }
    return gridfield;
  }

  float Evaluate(const GridField2D &gridfield, const Vector2D &p)
  {
    auto grid = gridfield.grid();
    auto values = gridfield.values();
    size_t i{};
    double x{}, y{};
    Point2Cell(grid,p,i,x,y);
    Info("Evaluate: i: " + str(i) + " x: " + str(x) + " y: " + str(y));
    
    const double v00 = values[i];
    const double v10 = values[i + 1];
    const double v01 = values[i + grid.xsize()];
    const double v11 = values[i + grid.xsize() + 1];

    return (1.0 - x) * (1.0 - y) * v00 +
        x * (1.0 - y) * v10 +
        (1.0 - x) * y * v01 +
        x * y * v11;
  }
}

#endif