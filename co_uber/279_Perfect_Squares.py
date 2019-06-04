#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/perfect-squares

Given a positive integer n, find the least number of perfect square
numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example,
given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return
2 because 13 = 4 + 9.

題: 494 類似
"""


class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        DP, top down from bottom up!
        e.g 14 sqt = 3
        """
        import math

        dp = [0]
        idx = 1

        while idx <= n:
            cnt = float("inf")

            for s in range(int(math.sqrt(idx)), 0, -1):
                cnt = min(cnt, dp[idx - s**2] + 1)
            dp.append(cnt)
            idx += 1

        return dp[n]

    def rewrite(self, n):
        """
        :type n: int
        :rtype: int
        dfs, 類似494
        needs memoir!
        """
        import math
        dp = dict()

        def dfs(idx, n):
            # ret: result cnt
            if n <= 0:
                return 0

            if dp.get((idx, n)):
                return dp[(idx, n)]

            result = float("inf")

            for i in range(idx, 0, -1):
                residule = n - i**2
                result = min(
                        dfs(int(math.sqrt(residule)), residule) + 1, result)

            dp[(idx, n)] = result

            return result

        return dfs(int(math.sqrt(n)), n)

def build():
    return 8935
    return 1001
    return 84410


if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(build()))
    print(s.rewrite(build()))
