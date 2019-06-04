#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/shortest-distance-from-all-buildings/

全部的都要.
You want to build a house on an empty land which reaches **all** buildings in
the shortest amount of distance.

You can only move up, down, left and right.
You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7

Explanation:
Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
the point (1,2) is an ideal empty land to build a house, as the total
travel distance of 3+3+1=7 is minimal. So return 7.
"""

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        TLE
        """
        from collections import defaultdict as dd

        direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
        rlen = len(grid)
        clen = len(grid[0])

        def bfs(i, j):
            """
            :ret: this node's distance count
            """
            visited = set()
            start = [(i, j)]
            lDis = -1
            dmap = dd(lambda : float("inf")) # key: loc, value: distance(minimum)

            while start:
                tmp = []
                lDis += 1

                # process
                for s in start:
                    visited.add(s)

                    for d in direction:
                        ni, nj = s[0] + d[0], s[1] + d[1]

                        if (ni, nj) in visited or \
                            ni < 0 or ni >= rlen or nj < 0 or nj >= clen or \
                            grid[ni][nj] == 2:
                            continue

                        if grid[ni][nj] == 1:
                            dmap[(ni, nj)] = min(dmap[(ni, nj)], lDis + 1)
                            continue

                        tmp.append((ni, nj))

                start = tmp

            return sum(dmap.values()) if len(dmap) == houses[0] else float("inf")

        mlen = float("inf")
        result = None
        spaces = []
        houses = [0]

        # check for how many houses
        for i in range(rlen):
            for j in range(clen):
                if grid[i][j] == 0:
                    spaces.append((i, j))
                elif grid[i][j] == 1:
                    houses[0] += 1

        for s in spaces:
            r = bfs(s[0], s[1])
            mlen = min(mlen, r)
            if mlen == r:
                result = (i, j)

        if mlen == float("inf"):
            return -1
        return mlen

    def rewrite(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Best solution
        Each 0 marks an empty land which you can pass by freely.
        Each 1 marks a building which you cannot pass through.
        Each 2 marks an obstacle which you cannot pass through.
        """

        direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
        bs = [(i, j)
                for i in range(len(grid))
                for j in range(len(grid[0]))
                if grid[i][j] == 1]

        space = [(i, j)
                    for i in range(len(grid))
                    for j in range(len(grid[0]))
                    if grid[i][j] == 0]

        def updateDP(i, j, dp):
            # bfs update

            root = set([(i, j, 0)]) # (m, n, distance)
            visited = set()

            while root:
                tmp = set()

                for m, n, dis in root:
                    visited.add((m, n))

                    for d in direction:
                        nm, nn = m + d[0], n + d[1]
                        if not 0 <= nm < len(grid) or \
                            not 0 <= nn < len(grid[0]) or \
                            grid[nm][nn] == 1 or \
                            grid[nm][nn] == 2 or \
                            (nm, nn) in visited:
                            continue
                        # no need to do min, since we are doing BFS
                        #  dp[nm][nn] = min(dp[nm][nn], dis + 1)
                        dp[nm][nn] = dis + 1
                        tmp.add((nm, nn, dis + 1))

                root = tmp


        dps = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
        for i, j in space:
            dps[i][j] = 0

        for i, j in bs:
            dp = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
            updateDP(i, j, dp)

            for m, n in space:
                dps[m][n] += dp[m][n]

        result = float("inf")
        for i in range(len(grid)):
            result = min(result, min(dps[i]))

        return result if result != float("inf") else -1

def build():
    return [[1]]
    return [[0,2,1],
            [1,0,2],
            [0,1,0]]
    return [[1,2,0]]
    return [[1,0,2,0,1],
            [0,0,0,0,0],
            [1,0,1,0,0],
            [1,0,1,0,0]]


if __name__ == "__main__":
    s = Solution()
    print(s.shortestDistance(build()))
    print(s.rewrite(build()))
