#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer
of the previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true


Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        convert matrix to a long sorted list then do a binary search.
        """
        import bisect as bi

        M = []

        for r in matrix:
            M.extend(r)

        idx = bi.bisect_left(M, target)

        if idx <= len(M) - 1 and M[idx] == target:
            return True

        return False

    def rewrite(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        for r in range(len(matrix)):
            if not matrix[r]:
                return False

            if target > matrix[r][-1]:
                continue
            # binary search at row level
            if target in matrix[r]:
                return True
            else:
                return False

        return False

def build():
    return [[1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]], 50


if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix(*build()))
    print(s.rewrite(*build()))
