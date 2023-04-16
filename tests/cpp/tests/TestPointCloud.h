#include "PointCloudMethods.h"
#include "VectorMethods.h"

TEST_CASE("PointCloud")
{
    std::vector<Vector3D> pts;
    pts.push_back(Vertex(0, 1, 0));
    pts.push_back(Vertex(1, 2, 0));
    pts.push_back(Vertex(2, 3, 0));
    pts.push_back(Vertex(3, 4, 0));
    pts.push_back(Vertex(4, 5, 0));
    pts.push_back(Vertex(5, 6, 0));
    pts.push_back(Vertex(6, 7, 0));
    pts.push_back(Vertex(7, 8, 0));
    pts.push_back(Vertex(8, 9, 1));

    std::vector<int> cls;
    cls.push_back(0);
    cls.push_back(1);
    cls.push_back(2);
    cls.push_back(3);
    cls.push_back(4);
    cls.push_back(5);
    cls.push_back(6);
    cls.push_back(7);
    cls.push_back(8);

    SECTION("Create vector PointCloud")
    {
        PointCloud pc = CreatePointCloud(pts, cls);
        REQUIRE(pc.points_size() == 9 * 3);
        REQUIRE(pc.classification(0) == 0);
        REQUIRE(pc.classification(5) == 5);
        REQUIRE(pc.classification(8) == 8);
    }

    SECTION("Create flat PointCloud")
    {
        std::vector<float> flat_points;
        for (auto &pt : pts)
        {
            flat_points.push_back(pt.x());
            flat_points.push_back(pt.y());
            flat_points.push_back(pt.z());
        }
        PointCloud pc = CreatePointCloud(flat_points, cls);
        REQUIRE(pc.points_size() == 9 * 3);
        REQUIRE(pc.classification(0) == 0);
        REQUIRE(pc.classification(5) == 5);
        REQUIRE(pc.classification(8) == 8);
    }
}
