INCLUDE(FindProtobuf)
include_directories(${PROTOBUF_INCLUDE_DIRS})
include_directories(${CMAKE_CURRENT_BINARY_DIR}/dtcc-model)
include_directories(${CMAKE_SOURCE_DIR}/dtcc-model)
set(CMAKE_CXX_FLAGS "-fPIC")
PROTOBUF_GENERATE_CPP(PROTO_SRC PROTO_HEADER dtcc.proto)
ADD_LIBRARY(dtccproto ${PROTO_HEADER} ${PROTO_SRC})


# PROTOBUF_GENERATE_PYTHON(PROTO_PY dtcc.proto)
# add_custom_target(python_protobuf ALL DEPENDS ${PROTO_PY})
# SET(PROTO_PY ${PROTO_PY} CACHE INTERNAL "PROTO_PY")

# message(STATUS "Cmake root: ${CMAKE_SOURCE_DIR}")
# INSTALL(FILES ${PROTO_PY} DESTINATION ${CMAKE_SOURCE_DIR}/datamodel_io/dtcc)
# message(STATUS "protobuf header and src: ${PROTO_PY} ${PROTO_HEADER} ${PROTO_SRC}")
