INCLUDE(FindProtobuf)
PROTOBUF_GENERATE_CPP(PROTO_SRC PROTO_HEADER dtcc.proto)
ADD_LIBRARY(dtccproto ${PROTO_HEADER} ${PROTO_SRC})
message(STATUS "protobuf header and src: ${PROTO_HEADER} ${PROTO_SRC}")