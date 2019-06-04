#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/climbing-stairs/description/

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.


Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        current_method = 1
        next_method = 1

        for _ in range(n):
            current_method, next_method = next_method, \
                current_method + next_method

        return current_method

    def rewrite(self, n):
        """
        :type n: int
        :rtype: int
        """
        from __builtin__ import xrange

        dp = dict()
        dp[0] = 1
        dp[1] = 1

        for i in xrange(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


def build():
    return 5


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(build()))
    print(s.rewrite(build()))
