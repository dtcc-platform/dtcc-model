cmake_minimum_required(VERSION 3.15)
project(dtcc-model)
set(PROJECT_VERSION 0.2.1)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS_ "-Wall -Werror -fPIC")

find_package(Protobuf REQUIRED)
set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)

INCLUDE(FindProtobuf)
PROTOBUF_GENERATE_CPP(PROTO_SRC PROTO_HEADER ${CMAKE_SOURCE_DIR}/src/proto/dtcc.proto)
message(STATUS "proto src: ${PROTO_SRC}")
message(STATUS "proto header: ${PROTO_HEADER}")
get_filename_component(PROTO_HEADER_DIR ${PROTO_HEADER} DIRECTORY)

include_directories(${PROTO_HEADER_DIR})
include_directories(${PROTOBUF_INCLUDE_DIRS})
include_directories(${CMAKE_SOURCE_DIR}/src/cpp/)
include_directories(${CMAKE_SOURCE_DIR}/src/cpp/protobuf)
MESSAGE(STATUS "protobuf include dirs: ${PROTOBUF_INCLUDE_DIRS}")
MESSAGE(STATUS "current binary dir: ${CMAKE_CURRENT_BINARY_DIR}")

ADD_LIBRARY(dtccproto SHARED ${PROTO_HEADER} ${PROTO_SRC})
set_target_properties(dtccproto PROPERTIES VERSION ${PROJECT_VERSION})
set_target_properties(dtccproto PROPERTIES PUBLIC_HEADER ${PROTO_HEADER})
target_link_libraries(dtccproto ${PROTOBUF_LIBRARY} Threads::Threads)
INSTALL(TARGETS dtccproto LIBRARY DESTINATION lib PUBLIC_HEADER DESTINATION include/dtcc_model)
INSTALL(DIRECTORY ${CMAKE_SOURCE_DIR}/src/cpp/include/ DESTINATION include/dtcc_model FILES_MATCHING PATTERN "*.h*")
