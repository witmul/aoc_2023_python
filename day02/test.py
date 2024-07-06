import unittest
from part01 import check_for_limit_spill
from part02 import get_max_cubes_per_color

class TestSolutionPart1Function(unittest.TestCase):
    def test_01(self):
        self.assertEqual(check_for_limit_spill('3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'), False)
    def test_02(self):
        self.assertEqual(check_for_limit_spill('1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue'), False)
    def test_03(self):
        self.assertEqual(check_for_limit_spill('8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'), True)
    def test_04(self):
        self.assertEqual(check_for_limit_spill('1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red'), True)
    def test_05(self):
        self.assertEqual(check_for_limit_spill('6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'), False)
    def test_06(self):
        self.assertEqual(check_for_limit_spill('13 red, 2 blue, 12 green; 19 green, 7 red; 17 green, 2 blue, 3 red; 6 blue, 11 red, 10 green; 6 red, 15 green, 3 blue; 6 blue, 20 green, 11 red'), True)

class TestSolutionPart2Function(unittest.TestCase):
    def test_01(self):
        self.assertEqual(get_max_cubes_per_color('3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'), 48)
    def test_02(self):
        self.assertEqual(get_max_cubes_per_color('1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue'), 12)
    def test_03(self):
        self.assertEqual(get_max_cubes_per_color('8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'), 1560)
    def test_04(self):
        self.assertEqual(get_max_cubes_per_color('1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red'), 630)
    def test_05(self):
        self.assertEqual(get_max_cubes_per_color('6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'), 36)


if __name__ == "__main__":
    unittest.main(verbosity=2)