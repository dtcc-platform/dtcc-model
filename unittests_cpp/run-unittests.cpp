#define CATCH_CONFIG_MAIN

#include "catch.hpp"

#include "protobuf/dtcc.pb.h"
#include "protobuf/include/VectorMethods.h"

using namespace DTCC;
TEST_CASE("Vectors")
{
    Vector3D v1{};
    v1.set_x(1.0);
    v1.set_y(2.0);
    v1.set_z(3.0);

    Vector3D v2{};
    v2.set_x(3.0);
    v2.set_y(2.0);
    v2.set_z(1.0);

    
    SECTION("Get and Set")
    {
        REQUIRE(v1.x() == 1.0);
        // REQUIRE(v1[1] == 2.0);

        v1.set_x(4.0);
        REQUIRE(v1.x() == 4.0);
        v1.set_x(1.0);
    }

    SECTION("Addition")
    {
        Vector3D v3 = v1 + v2;
        REQUIRE(v3.x() == 4.0);
        REQUIRE(v3.y() == 4.0);
        REQUIRE(v3.z() == 4.0);
    }


}