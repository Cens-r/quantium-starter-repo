#!/bin/bash

# Activate Virtual Environment
source ./venv/bin/activate

# Run all tests
pytest

# Retrieve the test(s) status
TEST_EXIT_CODE=$?

if [ $TEST_EXIT_CODE -eq 0 ]
then # All tests passed
  exit 0
else # One or more tests failed
  exit 1
fi