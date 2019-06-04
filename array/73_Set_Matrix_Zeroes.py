#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/set-matrix-zeroes/description/


Given a m x n matrix,
if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()

        for i, r in enumerate(matrix):
            if 0 in r:
                rows.add(i)

        for i, c in enumerate(zip(*matrix)):
            if 0 in c:
                cols.add(i)

        for e in rows:
            matrix[e][:] = [0] * len(matrix[0])

        for c in cols:
            for r in matrix:
                r[c] = 0


def build():
    return [
        [1, 0, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]


if __name__ == "__main__":
    nums = build()
    s = Solution()
    s.setZeroes(nums)
    print(nums)
