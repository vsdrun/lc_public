#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Say you have an array for which the ith element is the price of a given
stock on day i.

Design an algorithm to find the maximum profit.

1.
You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times)
with the following restrictions:

2.
You may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).

3.
After you sell your stock, you cannot buy stock on next day.
(ie, cooldown 1 day)

Example:
prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]

solution:
def maxProfit(self, prices):
    free = 0
    have = float('-inf')
    cool = float('-inf')

    for p in prices:
        free = max(free,cool)  # ready to buy.
        have = max(have, free - p)  # can sell
        cool = have + p  # rest
        # free, have, cool = max(free, cool), max(have, free - p), have + p

    return max(free, cool)
"""


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # free state. From previous free state and cool state.
        free = 0

        # have state. From previous have state and
        # free state stock - current day stock.
        have = float('-inf')

        # cool state. from have state + current day price.
        cool = float('-inf')

        for p in prices:
            # 前一個即什麼都不動...
            free, have, cool = max(free, cool), max(have, free - p), have + p

        return max(free, cool)


def build_input():
    return [1, 2, 3, 0, 2]


if __name__ == "__main__":
    n = build_input()

    s = Solution()
    result = s.maxProfit(n)

    # 3
    print(result)
