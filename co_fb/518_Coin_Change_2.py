#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/coin-change-2/description/

You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that
amount.

You may assume that you have infinite number of each kind of coin.

Note: You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer


Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4

Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1


Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.


Example 3:
Input: amount = 10, coins = [10]
Output: 1
"""


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in coins:
            for j in range(1, amount + 1):
               if j >= i:
                   dp[j] += dp[j - i]
        return dp[amount]

    def rewrite(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # prepare dp data
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for idx in range(1, len(dp)):
                if idx >= c:
                    dp[idx] += dp[idx - c]

        return dp[-1]

    def rewrite2(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int

        buttom up approach
        this implement is WRONG
        """
        dp = [0] * (amount + 1)
        dp[0] = 1  # i.e dollars minus to 0 has 1 form

        for i in range(1, len(dp)):
            visited = set()
            for c in coins:
                if (i - c) >= 0 and (i - c) not in visited:
                    dp[i] += dp[i - c]
                    visited.add(c)
        return dp[-1]

    def rewrite3(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        buttom up approach
        Go though the COINS instead of AMOUNT
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            # 由 coint 走的原因是避免重複count
            for i in range(1, len(dp)):
                if i >= c:
                    dp[i] += dp[i - c]

        return dp[-1]


def build():
    return 3, [1, 2]
    return 5, [1, 2, 5]

if __name__ == "__main__":
    s = Solution()
    print(s.change(*build()))
    print(s.rewrite(*build()))
    print(s.rewrite3(*build()))
