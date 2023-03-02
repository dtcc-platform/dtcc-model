#!/usr/bin/env bash


SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
echo "Running tests from ${SCRIPT_DIR}"
pushd ${SCRIPT_DIR}

mkdir -p build
cd build
echo "Running C++ unit tests!"
echo "-----------------------"
cmake ..
make
./unittests_cpp/run-unittests
popd
