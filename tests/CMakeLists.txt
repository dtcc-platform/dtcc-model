cmake_minimum_required(VERSION 3.5)
project(ModelTest)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS_ "-Wall -Werror -fPIC")

find_package(Protobuf REQUIRED)
set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)

message(STATUS "Cmake source dir " ${CMAKE_SOURCE_DIR})
message(STATUS "Cmake binary dir " ${CMAKE_BINARY_DIR})
INCLUDE(FindProtobuf)
PROTOBUF_GENERATE_CPP(PROTO_SRC PROTO_HEADER ${CMAKE_SOURCE_DIR}/../src/proto/dtcc.proto)
include_directories(${PROTOBUF_INCLUDE_DIRS})
include_directories(${CMAKE_SOURCE_DIR}/../src/cpp/)

ADD_LIBRARY(dtccproto ${PROTO_HEADER} ${PROTO_SRC})


ADD_SUBDIRECTORY(unittests_cpp)

MESSAGE(STATUS "protobuf include dirs: ${PROTOBUF_INCLUDE_DIRS}")
MESSAGE(STATUS "current binary dir: ${CMAKE_CURRENT_BINARY_DIR}")
