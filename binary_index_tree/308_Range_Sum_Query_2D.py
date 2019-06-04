#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/range-sum-query-2d-mutable/description/

https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/

https://brilliant.org/wiki/fenwick-tree/

https://leetcode.com/problems/range-sum-query-2d-mutable/discuss/75872/Python-94.5-Simple-sum-array-on-one-dimension-O(n)-for-both-update-and-sum
"""


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)


def build():
    return 1, 3


if __name__ == "__main__":
    s = Solution()
    result = s.licenseKeyFormatting(*build())

    print(result)
