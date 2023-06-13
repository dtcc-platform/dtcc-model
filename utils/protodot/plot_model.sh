#!/usr/bin/env bash

PROTODOT=./protodot
PROTOBUF=../../src/proto/dtcc.proto

# Check for protodot binary
if [ ! -x "$PROTODOT" ]; then
    echo "*** Missing protodot binary. Please copy the binary from"
    echo "*** https://github.com/seamia/protodot to this directory."
    exit 1
fi

# Check for graphviz
if ! command -v dot &> /dev/null; then
    echo "*** Missing dot command. Please install graphviz."
    exit
fi

# Generate visualization
$PROTODOT -src $PROTOBUF -output dtcc

# Update documentation
cp dtcc.dot.png ../../docs/images

# View image
open dtcc.dot.png
