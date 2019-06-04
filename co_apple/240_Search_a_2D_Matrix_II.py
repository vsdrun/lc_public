#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/search-a-2d-matrix-ii/description/

Write an efficient algorithm that searches for a value in an (m x n) matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.


For example,
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.
"""


class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        python's 'in' operator
        MyClass.__contains__(self, item)
        is doing bin-search!
        """
        return any(target in row for row in matrix
                   if row if row[-1] >= target)


def build_input():
    return [[]]
    return [[1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]]


if __name__ == "__main__":
    m = build_input()

    s = Solution()
    result = s.searchMatrix(m, 29)

    print(result)
