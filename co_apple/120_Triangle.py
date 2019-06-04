#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/triangle/description/

Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space,
where n is the total number of rows in the triangle.
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        """
        DP / array
        buttom up, use only 2 rows
        """

        dp = dict()
        dp[0] = list()
        dp[1] = list()

        for r in triangle:
            dp[1] = [float("inf")] * len(r)

            for idx in range(len(r)):

                if dp[0]:
                    # if idx == 0, 上一層只有 idx , 沒有idx - 1
                    one = float("inf") if idx == 0 else r[idx] + dp[0][idx - 1]
                    two = float("inf") if idx == len(
                        r) - 1 else r[idx] + dp[0][idx]

                    dp[1][idx] = min(one, two)
                else:
                    dp[1][idx] = r[idx]

            dp[0] = dp[1]
        return min(dp[1])


def build():
    return [[2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]]


if __name__ == "__main__":
    s = Solution()
    print(s.minimumTotal(build()))
