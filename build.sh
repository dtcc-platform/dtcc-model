#!/usr/bin/env bash

PROTO_DIR=./src/proto
CPP_DIR=./src/cpp/protobuf
PYTHON_DIR=./src/dtcc_model/

echo "Building C++ classes..."
protoc --cpp_out=$CPP_DIR $PROTO_DIR/dtcc.proto

echo "Building Python classes..."
protoc --python_out=$PYTHON_DIR $PROTO_DIR/dtcc.proto
