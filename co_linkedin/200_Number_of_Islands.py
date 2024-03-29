#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/number-of-islands/description/

Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically.

You may assume all four edges of the grid are all surrounded by water.

Example 1:
11110
11010
11000
00000
Answer: 1

Example 2:
11000
11000
00100
00011
Answer: 3

thought:
Sink and count the islands.

BFS
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        direction = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(i, j):
            if not 0 <= i < len(grid) \
               or not 0 <= j < len(grid[0]) \
               or grid[i][j] == '0':
                return

            grid[i][j] = '0'

            for d in direction:
                dfs(i + d[0], j + d[1])

        cnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '0':
                    dfs(i, j)
                    cnt += 1

        return cnt

    def numIslands_8dir(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and \
                    grid[i][j] == '1':

                grid[i][j] = '0'

                # 由一個1進入，將連接的都sink為0
                map(sink, (i + 1, i - 1, i, i, i - 1, i - 1, i + 1, i + 1),
                    (j, j, j + 1, j - 1, j - 1, j + 1, j - 1, j + 1))

                return 1

            return 0

        return sum(sink(i, j) for i in range(len(grid)) for j in
                   range(len(grid[i])))


def build():
    return [['1', '1', '0', '0', '0'],
              ['1', '1', '0', '0', '0'],
              ['0', '0', '1', '0', '0'],
              ['0', '0', '0', '1', '1']]

    return [['1', '1', '1', '1', '0'],
              ['1', '1', '0', '1', '0'],
              ['1', '1', '0', '0', '0'],
              ['0', '0', '0', '0', '0']]



if __name__ == "__main__":
    s = Solution()
    print(s.numIslands(build()))
    print(s.numIslands_8dir(build()))
