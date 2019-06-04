#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/spiral-matrix-ii/description/

Given a positive integer n, generate a
square matrix filled with elements from 1 to n^2 in spiral order.


Example:
Input: 3

Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 1:
            return []

        v = 1
        total = n**2
        d = 0  # ddir[d%4], d+=1
        i = 0
        j = -1

        ddir = ((0, 1), (1, 0), (0, -1),  (-1, 0))

        result = [[False] * n for _ in range(n)]

        while v <= total:
            # operation goes first...
            i += ddir[d % 4][0]
            j += ddir[d % 4][1]

            while 0 <= i < len(result) and 0 <= j < len(result[0]) and \
                    result[i][j] is False:
                result[i][j] = v
                v += 1
                i += ddir[d % 4][0]
                j += ddir[d % 4][1]

            i -= ddir[d % 4][0]
            j -= ddir[d % 4][1]
            d += 1
            i += ddir[d % 4][0]
            j += ddir[d % 4][1]

            while 0 <= i < len(result) and 0 <= j < len(result[0]) and \
                    result[i][j] is False:
                result[i][j] = v
                v += 1
                i += ddir[d % 4][0]
                j += ddir[d % 4][1]

            i -= ddir[d % 4][0]
            j -= ddir[d % 4][1]
            d += 1
            i += ddir[d % 4][0]
            j += ddir[d % 4][1]

            while 0 <= i < len(result) and 0 <= j < len(result[0]) and \
                    result[i][j] is False:
                result[i][j] = v
                v += 1
                i += ddir[d % 4][0]
                j += ddir[d % 4][1]

            i -= ddir[d % 4][0]
            j -= ddir[d % 4][1]
            d += 1
            i += ddir[d % 4][0]
            j += ddir[d % 4][1]

            while 0 <= i < len(result) and 0 <= j < len(result[0]) and \
                    result[i][j] is False:
                result[i][j] = v
                v += 1
                i += ddir[d % 4][0]
                j += ddir[d % 4][1]

            i -= ddir[d % 4][0]
            j -= ddir[d % 4][1]
            d += 1

        return result

    def rewrite(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A = [[0]*n for _ in range(n)]
        di, dj = 0, 1
        i, j = 0, 0

        for k in range(n**2):
            A[i][j] = k+1

            if A[(i+di) % n][(j+dj) % n]:
                di, dj = dj, -di

            i += di
            j += dj

        return A


def build():
    return 1


if __name__ == "__main__":
    s = Solution()
    print(s.generateMatrix(build()))
    print(s.rewrite(build()))
