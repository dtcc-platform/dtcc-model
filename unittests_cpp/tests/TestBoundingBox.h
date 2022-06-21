#include "protobuf/include/BoundingBoxMethods.h"

TEST_CASE("BoundingBox")
{
    SECTION("2D vector bounds")
    {
        std::vector<Vector2D> vecs;
        
        Vector2D v1;
        v1.set_x(1.0);
        v1.set_y(2.0);
        vecs.push_back(v1);

        Vector2D v2;
        v2.set_x(6.0);
        v2.set_y(2.0);
        vecs.push_back(v2);

        Vector2D v3;
        v3.set_x(5.0);
        v3.set_y(7.0);
        vecs.push_back(v3);

        Vector2D v4;
        v4.set_x(-1.0);
        v4.set_y(1.0);
        vecs.push_back(v4);


        auto bb = VectorBoundingBox(vecs);
        auto bb_P = bb.p();
        auto bb_Q = bb.q();
        REQUIRE(bb_P.x() == -1.0);
        REQUIRE(bb_P.y() == 1.0);
        REQUIRE(bb_Q.x() == 6.0);
        REQUIRE(bb_Q.y() == 7.0);
    }
}