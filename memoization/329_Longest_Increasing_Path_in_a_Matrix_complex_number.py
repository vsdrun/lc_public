#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions:
left, right, up or down.

You may NOT move diagonally or move outside of the boundary
(i.e. wrap-around is not allowed).

Example 1:
nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].


Example 2:
nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        #  nums = [
        #  [3, 4, 5],
        #  [3, 2, 6],
        #  [2, 2, 1]
        #  ]
        matrix = {i + j * 1j: val
                  for i, row in enumerate(matrix)
                  for j, val in enumerate(row)}

        # {0j: 3, (1+0j): 3, (2+0j): 2, 1j: 4, (1+1j): 2, (2+1j): 2, 2j: 5, (1+2j): 6, (2+2j): 1}

        print(matrix)

        length = {}

        for z in sorted(matrix, key=matrix.get):
            # 依據 dict的 value 排序，傳回key, i.e z==key
            print("z: {0}".format(z))
            # 注意! 此處
            # matrix[z] > matrix[Z]] 為關鍵!
            # 由最小往最大走
            # 但卻是到最大才有往小走得權力!
            # 這樣避免 length[z] 的 key值不存在!
            length[z] = 1 + max([length[Z]
                                 for Z in (z + 1, z - 1, z + 1j, z - 1j)
                                 if Z in matrix and matrix[z] > matrix[Z]] or
                                [0])

        return max(length.values() or [0])


def build():
    nums = [
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ]
    return nums


if __name__ == "__main__":
    nums = build()

    s = Solution()
    result = s.longestIncreasingPath(nums)

    print(result)
