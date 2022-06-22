#!/bin/bash

apt-get update && apt-get install -y \
    locales \
    sudo \
    build-essential \
    cmake\
    clang-format \
    clang-tidy \
    libprotobuf-dev\
    protobuf-compiler
