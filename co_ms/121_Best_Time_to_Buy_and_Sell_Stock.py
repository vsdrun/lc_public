#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Say you have an array for which the ith' element is the price of
a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and
sell one share of the stock), design an algorithm to find the maximum profit.

買最低賣最高

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5
(not 7-1 = 6, as selling price needs to be larger than buying price)


Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest = float("inf")
        maxc = 0

        for i in xrange(1, len(prices)):
            lowest = min(lowest, prices[i - 1])
            maxc = max(maxc, prices[i] - lowest)

        return maxc

    def maxProfit_2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        kadane algorithm
        利用差具有累加性的特性.
        """
        local_max = 0
        mmax = 0

        #  4, 2, 6 => 2 歸零代表 2 < 4, 則6幹麻要與4比差距??

        for i in xrange(1, len(prices)):
            local_max += prices[i] - prices[i - 1]

            local_max = max(0, local_max)
            mmax = max(mmax, local_max)

        return mmax

    def rewrite(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        from __builtin__ import xrange

        # 差距可以延續 it's transformable.
        tdiff = 0

        mmax = 0

        for i in xrange(1, len(prices)):

            diff = prices[i] - prices[i - 1]

            if tdiff + diff < 0:
                tdiff = 0
                continue

            tdiff += diff

            mmax = max(mmax, tdiff)

        return mmax


def build():
    return [7, 1, 5, 3, 6, 4]
    return [7, 1, 3]
    "-6 2"
    "-4"
    return [7, 6, 4, 3, 1]
    return [1, 3, 7, 1]


if __name__ == "__main__":

    s = Solution()
    result = s.maxProfit(build())

    print(result)

    result = s.maxProfit_2(build())

    print(result)

    result = s.rewrite(build())

    print(result)
