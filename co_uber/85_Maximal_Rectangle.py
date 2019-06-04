#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/maximal-rectangle/description/

Given a 2D binary matrix filled with 0's and 1's,
find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.

參考:
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix[0])

        # 用以代表一row的hight.
        height = [0] * (n + 1)  # 最後一個slot用來trigger final calculation.
        ans = 0

        for row in matrix:

            for i in xrange(n):
                # 每一個row累加 hight.
                height[i] = height[i] + 1 if row[i] == '1' else 0

            # 每一個row重新設定stack
            stack = [-1]

            for i in xrange(n + 1):
                # 最後一個height entry 為 0!!!
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)

                stack.append(i)

        return ans

    def rewrite(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        result = [0] * (len(matrix[0]) + 1)
        ans = 0

        for row in matrix:
            for idx in len(row):
                # 0 if this row 's row[idx] is 0
                result[idx] = result[idx] + 1 if row[idx] else 0

                # 2 pointer problem

            # 每一個row重新設定stack
            stack = [-1]

            for i in xrange(n + 1):
                # 最後一個height entry 為 0!!!
                while result[i] < result[stack[-1]]:
                    h = result[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)

                stack.append(i)

        return ans


def build():                 #       [          ]
    return [[0, 0, 1, 1, 0], #          [    ]
            [0, 1, 1, 1, 1], #             [ ]
            [1, 1, 1, 1, 1], # -> [1, 2, 3, 3, 2]
            [1, 0, 0, 1, 0]] # -> [2, 0, 0, 4, 0]
            [1, 0, 0, 1, 0]] # -> [3, 0, 0, 5, 2]

    return [[1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0]]


if __name__ == "__main__":

    s = Solution()
    print(s.maximalRectangle(build()))
    print(s.maxProfit_2(build()))
