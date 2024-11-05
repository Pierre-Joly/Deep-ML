#!/bin/bash

# Navigate to the project root directory
cd "$(dirname "$0")/.." || exit

# Add the project root to PYTHONPATH for imports
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Loop through each Python file in the tests directory
for test_file in ./tests/*.py; do
    echo "Running $test_file..."
    python "$test_file"
    
    # Check if the test failed
    if [ $? -ne 0 ]; then
        echo "Test failed: $test_file"
        exit 1  # Exit with an error code if any test fails
    fi
done

echo "All tests passed!"
