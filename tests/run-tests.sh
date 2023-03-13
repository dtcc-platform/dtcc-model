#!/usr/bin/env bash

echo "Running C++ unit tests"
echo "======================"
./cpp/bin/run-tests

echo "Running Python unit tests"
echo "========================="
python -m unittest discover python
