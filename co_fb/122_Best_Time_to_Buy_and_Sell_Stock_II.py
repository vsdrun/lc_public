#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

Say you have an array for which the ith element is the
price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).

買最低 賣最高

Example 1:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        概念?
        此天減昨天 大於0 累加.
        即便:
        1, 5, 3, 6, 7, 10
        3 - 10 or 3-6 , 6-7, 7-10 獲利是一樣的 因為沒有手續費...
        """
        result = 0

        for i in range(1, len(prices)):
            result += max(prices[i] - prices[i-1], 0)

        return result

    def rewrite(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        概念?
        就此天減昨天 若大於0 則賺.
        """

def build():
    return [1, 5, 3, 6, 7, 10]
    return [7,1,5,3,6,4]


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit(build()))
    print(s.rewrite(build()))
