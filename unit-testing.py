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
        self.assertEqual(list.min(), -9)
        testlist = []
        list = ListManipulator(testlist)
        self.assertEqual(list.min(), None)

    def testMax(self):
        pass

    def testRemove(self):
        pass


unittest.main()