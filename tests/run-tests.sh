#!/usr/bin/env bash


SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR
pushd $SCRIPT_DIR
echo "Running tests from ${SCRIPT_DIR}"

mkdir -p build
cd build
echo "Running C++ unit tests!"
echo "-----------------------"
cmake ..
make
./unittests_cpp/run-unittests
popd

echo "Running Python unit tests!"
echo "--------------------------"
python3 -m unittest discover -s unittests_py -p "test_*.py"
