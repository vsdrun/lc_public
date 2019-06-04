#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/min-cost-climbing-stairs/description/

On a staircase,
the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps.

You need to find minimum cost to reach the top of the floor,
and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.


Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0],
and only step on 1s, skipping cost[3].
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        from __builtin__ import xrange

        dp = [float("inf")] * (len(cost) + 2)  # consider out of cost to the top
        dp[0] = 0
        dp[1] = 0

        for i in xrange(1, len(cost) + 1):
            # 切換到dp 模式. sub problem 是啥?

            dp[i + 1] = min(dp[i] + cost[i - 1],
                            dp[i - 1] + cost[i - 2] if i > 1 else dp[i - 1])
        return dp[-1]


def build():
    return [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    return [10, 15, 20]


if __name__ == "__main__":

    s = Solution()
    print(s.minCostClimbingStairs(build()))
