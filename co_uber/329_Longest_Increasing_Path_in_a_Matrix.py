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


DP + DFS.
"""


class Solution(object):
    def longestIncreasingPath(self, matrix):
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        circle = set()
        direct = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]

            circle.add((i, j))
            lmax = 1

            for d in direct:
                x, y = i + d[0], j + d[1]

                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and \
                    (x, y) not in circle and matrix[i][j] > matrix[x][y]:
                    lmax = max(lmax, 1 + dfs(x, y))

            circle.remove((i, j))
            dp[i][j] = lmax
            return lmax


        return max(
            [dfs(i, j)
             for i in range(len(matrix)) for j in range(len(matrix[0]))]
            if matrix else [0])



def build():
    nums = [
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ]

    nums = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]

    nums = [
        [5, 6, 7],
        [4, 9, 8],
        [3, 2, 1]
    ]
    nums = []
    return nums


if __name__ == "__main__":
    s = Solution()
    print(s.longestIncreasingPath(build()))
