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

        result = []

        def pp(pos, direct):
            """
            :ret: last position, None means hit the end.
            """
            i, j = pos[0] + direct[0], pos[1] + direct[1]

            while 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and \
                    matrix[i][j] is not None:
                result.append(matrix[i][j])
                matrix[i][j] = None
                i += direct[0]
                j += direct[1]

            return i - direct[0], j - direct[1]

        ddir = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 右下左上

        root = ddir[:]
        last_pos = (0, -1)

        while root:

            while root:
                d = root.pop(0)
                last_pos = pp(last_pos, d)

                if len(result) == len(matrix) * len(matrix[0]):
                    return result

            root = ddir[:]

    def rewrite(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        ddir = ((0, 1), (1, 0), (0, -1), (-1, 0))

        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]

        cnt = 0
        i = 0
        j = -1

        total = len(matrix) * len(matrix[0])

        result = []

        while cnt != total:
            for d in ddir:
                # 先 operation 再判斷.
                i += d[0]
                j += d[1]

                while 0 <= i < len(matrix) and \
                        0 <= j < len(matrix[0]) and \
                        not visited[i][j]:

                    result.append(matrix[i][j])

                    visited[i][j] = True

                    cnt += 1

                    i += d[0]
                    j += d[1]

                i -= d[0]
                j -= d[1]

        return result


def build():
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
    print(s.rewrite(build()))
