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

