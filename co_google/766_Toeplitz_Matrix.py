#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/toeplitz-matrix/description/


A matrix is Toeplitz if every diagonal from top-left to
bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: True
Explanation:
1234
5123
9512

In the above grid, the diagonals are
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]",
and in each diagonal all elements are the same, so the answer is True.


Example 2:
Input: matrix = [[1,2],[2,2]]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.
"""


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        pop row by row!!
        """
        from __builtin__ import xrange

        init = [True]

        def test(mx):
            tmpinit = init[0]

            if init[0] is True:
                init[0] = False

            for i in xrange(len(mx[0]) if tmpinit else 1):
                var = mx[0][i]

                for r in xrange(1, len(mx)):
                    if i + r >= len(mx[0]):
                        continue

                    if mx[r][i + r] != var:
                        return False

            return True

        while matrix:
            if not test(matrix):
                return False

            matrix.pop(0)

        return True


def build():
    return [[44, 35, 39], [15, 44, 35], [17, 15, 44], [80, 17, 15], [43, 80, 0], [77, 43, 80]]
    return [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    return [[1, 9, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]


if __name__ == "__main__":
    s = Solution()
    print(s.isToeplitzMatrix(build()))
