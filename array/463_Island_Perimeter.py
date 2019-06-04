#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/island-perimeter/description/

You are given a map in form of a two-dimensional integer grid where 1
represents land and 0 represents water.

Grid cells are connected horizontally/vertically
(not diagonally).

The grid is completely surrounded by water, and there is
exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes"
(water inside that isn't connected to the water around the island)

One cell is a square with side length 1. The grid is rectangular, width
and height don't exceed 100.

Determine the perimeter of the island.
"""

class Solution(object):

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        翻轉四次
        一次只處理單一方向. 即處理北面。
        """
        from __builtin__ import xrange
        cnt = [0]

        def count(ary):
            for i in xrange(len(ary)):
                if i == 0:
                    cnt[0] = cnt[0] + sum(ary[i])
                    continue

                for j in xrange(len(ary[0])):
                    if ary[i][j] == 1:
                        if ary[i - 1][j] != 1:
                            cnt[0] = cnt[0] + 1

        for _ in xrange(4):
            count(grid)
            grid = zip(*grid[::-1])

        return cnt[0]

    def rewrite(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        [0, 1, 0, 0]

        [0, 0, 1, 0, 0]
        [0, 1, 0, 0, 0]
        """
        total = 0

        for r in grid:
            r1 = [0] + r
            r2 = r + [0]
            for i in range(len(r1)):
                if r1[i] ^ r2[i]:
                    total += 1

        grid = map(list, zip(*grid))

        for r in grid:
            r1 = [0] + r
            r2 = r + [0]
            for i in range(len(r1)):
                if r1[i] ^ r2[i]:
                    total += 1

        return total

def build():
    return [[0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]]


if __name__ == "__main__":
    r = Solution()
    print(r.rewrite(build()))
