#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/cherry-pickup/

In a N x N grid representing a field of cherries,
each cell is one of three possible integers.


0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.

Your task is to collect maximum number of cherries possible by following
the rules below:

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or
down through valid path cells (cells with value 0 or 1);

After reaching (N-1, N-1),
returning to (0, 0) by moving left or up through valid path cells;

When passing through a path cell containing a cherry,
you pick it up and the cell becomes an empty cell (0);

If there is no valid path between (0, 0) and (N-1, N-1),
then no cherries can be collected.

Example 1:
Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]

[[0, 1, -1],
 [5, 1, -1],
 [4, 2,  3]]
Output: 5

Explanation:
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip,
and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].

Then, the player went left, up, up,
left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.

Note:
grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.

https://leetcode.com/problems/cherry-pickup/discuss/109906/Annotated-C%2B%2B-DP-Solution

https://www.cnblogs.com/grandyang/p/8215787.html
"""

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
         O(N^3)
        """
        def dfs(i1, j1, i2, j2):
            if (i1, j1, i2, j2) in dp:
                return dp[(i1, j1, i2, j2)]

            if i1 == N or j1 == N or i2 == N or j2 == N:
                return -1

            if i1 == j1 == i2 == j2 == N-1:
                return grid[-1][-1]

            if grid[i1][j1] == -1 or grid[i2][j2] == -1:
                return -1

            dd = dfs(i1+1, j1, i2+1, j2)
            rr = dfs(i1, j1+1, i2, j2+1)

            dr = dfs(i1+1, j1, i2, j2+1)
            rd = dfs(i1, j1+1, i2+1, j2)

            maxComb = max([dd, dr, rd, rr])

            # find if there is a way to reach the end
            if maxComb == -1:
                out = -1
            else:
                # same cell, can only count this cell once
                if i1 == i2 and j1 == j2:
                    out = maxComb + grid[i1][j1]
                # different cell, can collect both
                else:
                    out = maxComb + grid[i1][j1] + grid[i2][j2]

            # cache result
            dp[(i1, j1, i2, j2)] = out
            return out

        if grid[-1][-1] == -1:
            return 0

        # set up cache
        dp = {}
        N = len(grid)
        result = max(dfs(0, 0, 0, 0), 0)
        #  print("dp: {}".format(dp))
        return result

    def rewrite(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """



def build():
    return [
        [0, 1, -1],
        [1, 0, -1],
        [1, 1,  1]]

     #  [0, 1, -1],
     #  [1, 2, -1],
     #  [3, 2,  1]]

if __name__ == "__main__":
    s = Solution()
    print(s.cherryPickup(build()))
