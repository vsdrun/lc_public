#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/coin-change/description/

You are given coins of different denominations and a total
amount of money amount.

Write a function to compute the fewest number of coins that you
need to make up that amount.

If that amount of money cannot be made up
by any combination of the coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1


Example 2:
Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        # [0, 1, 2, 3, 4, 5]
        for rhs in range(1, len(dp)):
            dp[rhs] = min(
                    dp[rhs - c] if rhs - c >= 0 else float("inf")
                    for c in coins
                    ) + 1

        return dp[-1] if dp[-1] != float("inf") else -1


def build():
    return [1, 2, 5], 11
    return [5], 11


if __name__ == "__main__":

    s = Solution()
    print(s.coinChange(*build()))
