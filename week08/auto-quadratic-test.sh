#!/bin/bash

echo "##########################"
echo "### Testing quadratic.py"
echo "##########################\n"
count=0
# number of test cases run so far
# Assume all `.in` and `.out` files are located in a separate `tests` directory
for test in tests/*.in; do
	name=$(basename $test .in)
	expected=tests/$name.out
	python3 quadratic.py < $test | diff - $expected | cat -A || echo "Test $name: failed!\n"
	count=$((count+1))
done

echo "Finished running $count tests!"

