# ella ballou
# software development fundamentals
# programming lab 10

import unittest


class ListManipulator:
    def __init__(self, list):
        self.list = list

    def min(self):
        if len(self.list) == 0:
            return None

        min = self.list[0]
        for item in self.list:
            if item < min:
                min = item
        return min

    def max(self):
        if len(self.list) == 0:
            return None

        max = self.list[0]
        for item in self.list:
            if item > max:
                max = item
        return max

    def remove(self, value):
        to_remove = []
        for i, item in enumerate(self.list):
            if item == value:
                to_remove.append(i)

        removed_count = 0
        for index in to_remove:
            self.list.pop(index - removed_count)
            removed_count += 1


class TestListManipulator(unittest.TestCase):
    def testMin(self):
        testlist = [-2, -7, -9, 0, 4, 6, -1, 7, 3, 2]  # random set of positive and negative integers
        list = ListManipulator(testlist)
        self.assertEqual(list.min(), -9)  # smallest number in the list is -9, so it should return -9
        testlist = []
        list = ListManipulator(testlist)
        self.assertEqual(list.min(), None)  # when there are no items in the list, it should return None

    def testMax(self):
        testlist = [-5, 4, -2, 9, 8, -7, -4, -6, -9, 10]  # random set of positive and negative integers
        list = ListManipulator(testlist)
        self.assertEqual(list.max(), 10)  # the largest number in the set is 10, should return 10
        testlist = []
        list = ListManipulator(testlist)
        self.assertEqual(list.max(), None)  # when there are no items in the list, it should return None

    def testRemove(self):
        testlist = [2, 1, 5, 1, 1, 10, -5, 10, 0, 8]  # original list, random set
        list = ListManipulator(testlist)
        list.remove(1)  # removes all 1's from the list
        self.assertEqual(list.list, [2, 5, 10, -5, 10, 0, 8])  # the list should be equal to the testlist w all 1's removed
        testlist = []  # a list with no values
        list = ListManipulator(testlist)
        list.remove(0)  # removes all 0's from that blank list (does nothing)
        self.assertEqual(list.list, [])  # list should stay empty


unittest.main()