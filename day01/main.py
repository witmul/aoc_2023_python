from part01 import main as main_p_01
from part02 import main as main_p_02
import unittest
from test import TestSolutionPart1Function, TestSolutionPart2Function

# try to load all testcases from given module, hope your testcases are extending from unittest.TestCase
suite_01 = unittest.TestLoader().loadTestsFromTestCase(TestSolutionPart1Function)
print ("---- Running tests for first part ----")
# run all tests with verbosity 
unittest.TextTestRunner(verbosity=2).run(suite_01)
print ("---- Stop running tests for first part ----")

print ("\n")

print ("---- Result for first part ----")
print(main_p_01("day01\input.txt"))

print ("\n")

suite_02 = unittest.TestLoader().loadTestsFromTestCase(TestSolutionPart2Function)
print ("---- Running tests for second part ----")
# run all tests with verbosity 
unittest.TextTestRunner(verbosity=2).run(suite_02)
print ("---- Stop running tests for second part ----")

print ("\n")

print ("---- Result for second part ----")
print(main_p_02("day01\input.txt"))