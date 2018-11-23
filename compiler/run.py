import os
import subprocess
from run_test import run_single_test

tests = os.listdir("./tests/")  # get all files' and folders' names in the current directory

failed_tests = []
passed_tests = []

for test in tests:
    output = run_single_test(test,1)
    if output == 0:
        passed_tests.append(test)
    else:
        failed_tests.append(test)

print "Passed tests"
print passed_tests
print "Failed tests"
print failed_tests
