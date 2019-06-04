#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/01-matrix/description/

Given a matrix consists of 0 and 1,
find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:
Input:
0 0 0
0 1 0
0 0 0

Output:
0 0 0
0 1 0
0 0 0

Example 2:
Input:
0 0 0
0 1 0
1 1 1

Output:
0 0 0
0 1 0
1 2 1

Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.


旋轉的藝術...

BFS有幾個特性:
    1. 剝洋蔥 一次一層
    2. 為最近

概念1:
先由左上到右下
再由右下至左上


概念2:
BFS. 將1設定為Max.
初始將0放入bfs queue.
接著4方放入queue iff 四方的value > 目前的location value + 1.
由小->大BFS.
"""


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        概念1:
        """
        # only init value which is 1
        answer = [[90000 * x for x in row] for row in matrix]

        for _ in range(4):
            for row in answer:
                for j in range(1, len(row)):
                    row[j] = min(row[j], row[j - 1] + 1)

            # 必須為 answer[::-1] 不然不是90度旋轉!
            answer = map(list, zip(*answer[::-1]))

        return answer

    def rewrite(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        概念1:
        """
        from __builtin__ import xrange

        def maxfunc(i, j):
            matrix[i][j] = float("inf")

        # mark 1 into large
        [map(maxfunc, (i,), (j,))
         for i in xrange(len(matrix)) for j in xrange(len(matrix[0]))
         if matrix[i][j] == 1]

        for _ in xrange(4):
            for row in matrix:
                for i in xrange(1, len(row)):
                    row[i] = min(row[i], row[i - 1] + 1)

            matrix[:] = map(list, zip(*matrix[::-1]))
        return matrix


def build():
    result = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
              [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
              [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
              [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
              [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
              [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
              [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
              [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]

    result = [[0, 0, 0],
              [0, 1, 1],
              [1, 1, 1]]

    return result


if __name__ == "__main__":

    s = Solution()
    result = s.updateMatrix(build())
    print(result)
    result = s.rewrite(build())
    print(result)
