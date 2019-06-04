#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/pacific-atlantic-water-flow/description/

Given an (m X n) matrix of non-negative integers representing the
height of each unit cell in a continent,
the "Pacific ocean" touches the left and top edges of the matrix and
the "Atlantic ocean" touches the right and bottom edges.


Water can only flow in four directions (up, down, left, or right)
from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both
the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.

Example:
Given the following 5x5 matrix:

Pacific ~   ~   ~   ~   ~
   ~  1   2   2   3  (5) *
   ~  3   2   3  (4) (4) *
   ~  2   4  (5)  3   1  *
   ~ (6) (7)  1   4   5  *
   ~ (5)  1   1   2   4  *
      *   *   *   *   * Atlantic

Return:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
(positions with parentheses in above matrix).
"""

"""
Idea:
1. test each node with Pacific: up/left
2. test each node with Atlantic: down/right
3. use memoir
"""


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        Buttom up approach.
        Why?
        Because it's simple.
        If goes through top-down approach, the solutions would be endless,
        since you have to check if we hit the boundary of pacific or atlantic,
        which is unknown.
        Besides, if goes through top-down, we have to update the node with
        hit boundary result upward as well.

        With buttom up approach, the start is limited.
        https://discuss.leetcode.com/topic/66065/python-dfs-bests-85-tips-for-all-dfs-in-matrix-question
        """
        from __builtin__ import xrange

        if not matrix:
            return []

        X = len(matrix[0])
        Y = len(matrix)

        p_walked = [[False for _ in xrange(X)] for _ in xrange(Y)]
        a_walked = [[False for _ in xrange(X)] for _ in xrange(Y)]

        direction = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(x, y, walked):
            # 表示可以到達!
            walked[y][x] = True

            for d in direction:
                next_x = x + d[0]
                next_y = y + d[1]

                if next_x < 0 or next_y < 0 or \
                        next_x > X - 1 or next_y > Y - 1 or \
                        walked[next_y][next_x] or \
                        matrix[next_y][next_x] < matrix[y][x]:
                        # walked 也作為 visited 用!
                    continue

                dfs(next_x, next_y, walked)

        for n in xrange(X):
            # 上/下 P/A
            # pacific
            dfs(n, 0, p_walked)
            # atlantic
            dfs(n, Y - 1, a_walked)

        for n in xrange(Y):
            # 左/右 P/A
            # pacific
            dfs(0, n, p_walked)
            # atlantic
            dfs(X - 1, n, a_walked)

        result = []

        # A 可到 且 P 可到的收集起來.
        for x in xrange(len(matrix[0])):
            for y in xrange(len(matrix)):
                if p_walked[y][x] and a_walked[y][x]:
                    result.append([y, x])

        return result

    def rewrite(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []

        from __builtin__ import xrange

        # create 2 graph for P and A
        # 要注意!!! 每個row必須為獨立!!! 要小心初始化的方式!
        pgraph = [[0 for _ in xrange(len(matrix[0]))]
                  for _ in xrange(len(matrix))]
        agraph = [[0 for _ in xrange(len(matrix[0]))]
                  for _ in xrange(len(matrix))]

        direction = ((1, 0), (-1, 0), (0, -1), (0, 1))

        def dfs(i, j, graph):
            graph[i][j] = 1

            for d in direction:
                ni = i + d[0]
                nj = j + d[1]

                if ni < 0 or ni >= len(matrix) or \
                        nj < 0 or nj >= len(matrix[0]) or \
                        graph[ni][nj] or \
                        matrix[ni][nj] < matrix[i][j]:

                    continue

                dfs(ni, nj, graph)

        # from up and down
        for j in xrange(len(matrix[0])):
            # pacific
            dfs(0, j, pgraph)

            # atlantic
            dfs(len(matrix) - 1, j, agraph)

        # from left and right
        for i in xrange(len(matrix)):
            # pacific
            dfs(i, 0, pgraph)

            # atlantic
            dfs(i, len(matrix[0]) - 1, agraph)

        result = []

        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if agraph[i][j] and pgraph[i][j]:
                    result.append([i, j])
        return result

    def rewrite2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []

        dmap_A = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        dmap_P = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        direction = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(m, n, dmap):
            if dmap[n][m]:
                return

            dmap[n][m] = 1

            for d in direction:
                next_m = m + d[0]
                next_n = n + d[1]

                if next_m < 0 or next_m >= len(matrix[0]) or \
                        next_n < 0 or next_n >= len(matrix) or \
                        matrix[n][m] > matrix[next_n][next_m]:
                    continue

                dfs(next_m, next_n, dmap)

        # P
        for m in range(len(matrix[0])):
            dfs(m, 0, dmap_P)

        for n in range(len(matrix)):
            dfs(0, n, dmap_P)

        # A
        for m in range(len(matrix[0])):
            dfs(m, len(matrix) - 1, dmap_A)

        for n in range(len(matrix)):
            dfs(len(matrix[0]) - 1, n, dmap_A)

        result = []

        for m in range(len(matrix[0])):
            for n in range(len(matrix)):
                if dmap_A[n][m] == 1 and dmap_P[n][m] == 1:
                    result.append([n, m])
        return result


def build():
    result = [[1, 2, 2, 3, 5],
              [3, 2, 3, 4, 4],
              [2, 4, 5, 3, 1],
              [6, 7, 1, 4, 5],
              [5, 1, 1, 2, 4]]
    result = [[1, 2, 2],
              [3, 4, 5],
              [6, 1, 1]]
    result = [[1, 1],
              [1, 1],
              [1, 1]]

    result = [[1, 2, 2, 3, 5],
              [3, 2, 3, 4, 4],
              [2, 4, 5, 3, 1],
              [6, 7, 1, 4, 5],
              [5, 1, 1, 2, 4]]
    return result


if __name__ == "__main__":
    s = Solution()
    print(s.pacificAtlantic(build()))
    print(s.rewrite(build()))
    print(s.rewrite2(build()))
