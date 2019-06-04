#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

Your are given an array of integers prices,
for which the i-th element is the price of a given stock on day i;
and a non-negative integer fee representing a transaction fee.


You may complete as many transactions as you like,
but you need to pay the transaction fee for each transaction.
You may not buy more than 1 share of a stock at a time
(ie. you must sell the stock share before you buy again.)


Return the maximum profit you can make.


Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Note:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.


https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems


https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108901/C++-O(n)-time-O(1)-space
"""


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        概念:
        買: 負的price , -prices[i]
        賣: 正的price + previous買的負的prices -prices[0] 減去手續費.
        """

        from __builtin__ import xrange

        buyin = -prices[0]
        for_next_buy = 0
        sell = 0

        for i in xrange(1, len(prices)):
            # 買 + 之前的獲利 , 選擇最好的買點
            # 初始 buyin == -prices[0]
            # 這次不處理next_buy, 留在下一個loop跑.
            # max也代表賣的初始價格最低
            for_next_buy = max(buyin, -prices[i] + sell)

            # 目前賣的獲利
            sell = max(sell, prices[i] - fee + buyin)

            # 下一個 loop 買
            buyin = for_next_buy

        return sell

    def rewrite(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        概念:
        買: 負的price , -prices[i]
        賣: 正的price + previous買的負的prices -prices[0] 減去手續費.
        """
        from __builtin__ import xrange

        # dp , try them all.
        # buttom up

        # buy first, sell later
        # dp as Sell at this point's max value
        buyin = -prices[0]
        next_buy = 0
        sell = 0

        for i in xrange(1, len(prices)):
            next_buy = max(buyin, -prices[i] + sell)

            sell = max(sell, prices[i] - fee + next_buy)

            buyin = next_buy

        return sell


def build():
    return [1, 3, 7, 2, 9], 2
    return [1, 3, 2, 8, 4, 9], 2


if __name__ == "__main__":

    s = Solution()
    print(s.maxProfit(*build()))
