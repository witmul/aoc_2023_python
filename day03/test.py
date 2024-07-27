import unittest
from part01 import main


class TestSolutionPart1Function(unittest.TestCase):
    def test_01(self):
        self.assertEqual(main("day03/test_input.txt"), 4361)

if __name__ == "__main__":
    unittest.main(verbosity=2)