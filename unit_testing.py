# ella ballou
# software development fundamentals
# programming lab 10

# github.com/ella-ballou/unit-testing   <-- link to repository

import unittest
from ListManipulator import ListManipulator


class TestListManipulatorMin(unittest.TestCase):
    def test_1(self):
        testlist = [-2, -7, -9, 0, 4, 6, -1, 7, 3, 2]  # random set of positive and negative integers
        list = ListManipulator(testlist)
        self.assertEqual(list.min(), -9)  # smallest number in the list is -9, so it should return -9

    def test_2(self):
        testlist = []  # list with no items
        list = ListManipulator(testlist)
        self.assertEqual(list.min(), None)  # when there are no items in the list, it should return None

    def test_3(self):
        testlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # all inputs are the same digit
        list = ListManipulator(testlist)
        self.assertEqual(list.min(), 0)  # all numbers are the same, should still return 0


class TestListManipulatorMax(unittest.TestCase):
    def test_1(self):
        testlist = [-5, 4, -2, 9, 8, -7, -4, -6, -9, 10]  # random set of positive and negative integers
        list = ListManipulator(testlist)
        self.assertEqual(list.max(), 10)  # the largest number in the set is 10, should return 10

    def test_2(self):
        testlist = []  # list with no values inputted
        list = ListManipulator(testlist)
        self.assertEqual(list.max(), None)  # when there are no items in the list, it should return None

    def test_3(self):
        testlist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]  # list of all the same value entered
        list = ListManipulator(testlist)
        self.assertEqual(list.max(), 10)  # even though all inputs were the same, it should still return 10


class TestListManipulatorRemove(unittest.TestCase):
    def test_1(self):
        testlist = [2, 1, 5, 1, 1, 10, -5, 10, 0, 8]  # original list, random set
        list = ListManipulator(testlist)
        list.remove(1)  # removes all 1's from the list
        self.assertEqual(list.list, [2, 5, 10, -5, 10, 0, 8])  # list should be equal to the testlist w all 1's removed

    def test_2(self):
        testlist = []  # a list with no values
        list = ListManipulator(testlist)
        list.remove(0)  # removes all 0's from that blank list (does nothing)
        self.assertEqual(list.list, [])  # list should stay empty

    def test_3(self):
        testlist = [-2, -3, -9, -8, -2, -9, 8, 10, -3, -8]  # a random list of integers
        list = ListManipulator(testlist)
        list.remove(6)  # removes all 6's from list
        self.assertEqual(list.list, testlist)  # the list shouldn't change, because there were no 6's in the list

    def test_4(self):
        testlist = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]  # a list with all the same values
        list = ListManipulator(testlist)
        list.remove(4)  # removes all 4's from list
        self.assertEqual(list.list, [])  # the list should become empty, because there are only 4's in list


unittest.main()
