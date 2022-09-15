#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo "Running C++ unit tests!"
echo "-----------------------"

${SCRIPT_DIR}/unittests_cpp/bin/run-unittests

#echo ${SCRIPT_DIR}/unittests_py/test.py

echo "Running Python unit tests!"
echo "-----------------------"
python3 -m unittest ${SCRIPT_DIR}/unittests_py/test.py
