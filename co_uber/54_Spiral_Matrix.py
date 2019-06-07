#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/spiral-matrix/description/

Given a matrix of (m x n) elements (m rows, n columns),
return all elements of the matrix in spiral order.


Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]


Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        direct = ((0, 1), (1, 0), (0, -1), (-1, 0))
        result = []

        def bfs(i, j):
            root = [i, j]
            d = 0

            while len(result) < len(matrix) * len(matrix[0]):

                while 0 <= root[0] < len(matrix) and \
                    0 <= root[1] < len(matrix[0]) and \
                    matrix[root[0]][root[1]] is not None:

                        result.append(matrix[root[0]][root[1]])
                        matrix[root[0]][root[1]] = None
                        root[0], root[1] = \
                            root[0] + direct[d%4][0], root[1] + direct[d%4][1]

                root[0], root[1] = \
                    root[0] - direct[d%4][0], root[1] - direct[d%4][1]

                d += 1

                root[0], root[1] = \
                    root[0] + direct[d%4][0], root[1] + direct[d%4][1]

        bfs(0, 0)
        return result

def build():
    return []
    return [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]


if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder(build()))
