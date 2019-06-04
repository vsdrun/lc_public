#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/number-of-distinct-islands/description/

Given a non-empty 2D array grid of 0's and 1's,
an island is a group of 1's (representing land) connected 4-directionally
(horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands.
An island is considered to be the same as another if and only if
one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.

Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.


Notice that:
11
1
and
 1
11
are considered different island shapes,
because we do not consider reflection / rotation.
"""


class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        distict 想到 hashmap 1:1
        island 想到 dfs traverse

        重點是 signature 表示 island
        How?
        consistency signature.
        """
        from __builtin__ import xrange

        drt = ((0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U'))

        def signature(x, y, sig):
            """
            :param sig: str
            :return: sig
            """
            if len(grid) - 1 < x or x < 0 or y < 0 or \
                    len(grid[0]) - 1 < y or grid[x][y] == -1 or \
                    grid[x][y] == 0:
                return "-"  # 重要!!! 即使碰到邊際 也要有 signature!

            grid[x][y] = -abs(grid[x][y])

            for xx, yy, ss in drt:
                sig += signature(x + xx, y + yy, ss)

            return sig

        dset = set()

        for x in xrange(len(grid)):
            for y in xrange(len(grid[0])):
                if grid[x][y] == 1:
                    dset.add(signature(x, y, '1'))

        return len(dset)


def build():
    return \
        [[0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
         [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    return [[1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1]]
    return [[1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]]


if __name__ == "__main__":
    s = Solution()
    print(s.numDistinctIslands(build()))
