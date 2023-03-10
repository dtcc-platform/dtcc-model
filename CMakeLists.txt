cmake_minimum_required(VERSION 3.5)
project(ModelTest)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS_ "-Wall -Werror")

set(pybind11_DIR /usr/lib/cmake/pybind11)
find_package(pybind11 REQUIRED)

find_package(Protobuf REQUIRED)
set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)


ADD_SUBDIRECTORY(protobuf)


include_directories(${PROTOBUF_INCLUDE_DIRS}) 
include_directories(${CMAKE_CURRENT_BINARY_DIR})
include_directories(${CMAKE_SOURCE_DIR})
include_directories(${CMAKE_CURRENT_BINARY_DIR}/dtcc-model)
include_directories(/usr/local/include)

add_subdirectory(datamodel_io)

ADD_SUBDIRECTORY(tests/unittests_cpp)

MESSAGE(STATUS "protobuf include dirs: ${PROTOBUF_INCLUDE_DIRS}")
MESSAGE(STATUS "current binary dir: ${CMAKE_CURRENT_BINARY_DIR}")

get_property(dirs DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY INCLUDE_DIRECTORIES)
foreach(dir ${dirs})
  message(STATUS "dir='${dir}'")
endforeach()
