cmake_minimum_required(VERSION 3.5)
project(ModelTest)

set(CMAKE_CXX_FLAGS_ "-Wall -Werror")
find_package(Protobuf REQUIRED)
set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)


ADD_SUBDIRECTORY(protobuf)


include_directories(${PROTOBUF_INCLUDE_DIRS}) 
include_directories(${CMAKE_CURRENT_BINARY_DIR})
include_directories(${CMAKE_SOURCE_DIR})
include_directories(${CMAKE_CURRENT_BINARY_DIR}/dtcc-model)

ADD_SUBDIRECTORY(unittests_cpp)

MESSAGE(STATUS "protobuf include dirs: ${PROTOBUF_INCLUDE_DIRS}")
MESSAGE(STATUS "current binary dir: ${CMAKE_CURRENT_BINARY_DIR}")

get_property(dirs DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY INCLUDE_DIRECTORIES)
foreach(dir ${dirs})
  message(STATUS "dir='${dir}'")
endforeach()
