#!/usr/bin/env bash


SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
pushd ${SCRIPT_DIR}
echo "Running C++ unit tests!"
echo "-----------------------"

./unittests_cpp/bin/run-unittests


