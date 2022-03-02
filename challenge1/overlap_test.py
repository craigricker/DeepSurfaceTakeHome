import unittest

from overlap import *


class TestOverlapFunctionWithInt(unittest.TestCase):
    def test_single_list_sent(self):
        self.assertCountEqual([4], overlap([[4]]))

    def test_empty_list_sent(self):
        self.assertCountEqual([], overlap([]))

    def test_single_empty_list_sent(self):
        self.assertCountEqual([], overlap([[1], [1], []]))

    def test_handles_repeats(self):
        self.assertCountEqual([1], overlap([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))

    def test_100_percent_overlap(self):
        self.assertCountEqual([1, 2, 3], overlap([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))

    def test_many_lists_passed(self):
        self.assertCountEqual([1, 2, 3], overlap([[1, 2, 3]] * 100))

    def take_home_example(self):
        self.assertCountEqual([7, 4, 2, 3], [[8, 1, 2, 4, 5, 2, 7, 1, 9, 4, 2], [7, 4, 2, 3, 0, 6],
                                             [1, 2, 4, 5, 2, 7, 1, 9, 4, 2, 3, 9, 9, 8]])


class TestOverlapFunctionWithStr(unittest.TestCase):
    def test_single_list_sent(self):
        self.assertCountEqual(["hello"], overlap([["hello"]]))

    def test_handles_repeats(self):
        self.assertCountEqual(["y"], overlap([["y", 'y', 'y'], ['y', 'y', 'y']]))

    def test_100_percent_overlap(self):
        arg = ['a', 'b', 'c']
        self.assertCountEqual(arg, overlap([arg, arg, arg]))

    def test_many_lists_passed(self):
        arg = ['a', 'b', 'c']
        self.assertCountEqual(arg, overlap([arg] * 100))
