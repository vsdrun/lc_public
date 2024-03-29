#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/shopping-offers/description/


In LeetCode Store,
there are some kinds of items to sell.
Each item has a price.

However, there are some special offers,
and a special offer consists of one or more different
kinds of items with a sale price.

You are given the each item's price,
a set of special offers, and the number we need to buy for each item.

The job is to output the lowest price you have to pay for **exactly** certain
items as given, where you could make optimal use of the special offers.

Each special offer is represented in the form of an array,
the last number represents the price you need to pay for this special offer,
other numbers represents how many specific items you could get
if you buy this offer.

***可重複使用
You could use any of special offers as many times as you want.

Example 1:
Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
Output: 14
Explanation
There are two kinds of items, A and B.
Their prices are $2 and $5 respectively.
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B.
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2),
and $4 for 2A.

Example 2:
Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
Output: 11
Explanation:
The price of A is $2, and $3 for B, $4 for C.
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C.
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B
(special offer #1), and $3 for 1B, $4 for 1C.

You cannot add more items, though only $9 for 2A ,2B and 1C.


Note:
There are at most 6 kinds of items, 100 special offers.
For each item, you need to buy at most 6 of them.
You are not allowed to buy more items than you want, even if that would lower the overall price.
"""


class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """

        memoir = {}  # key 為每個item needs的數量. value: total price

        def dfs(needs):
            #  先找 local totol.  區域最佳解.
            total = sum(needs[i] * price[i]
                        for i in range(len(needs)))  # cost without special

            for s in special:
                sprice = s[-1]

                # for this special, what's the quantity still be needed for
                # each item.
                tmp = [needs[j] - s[j] for j in range(len(needs))]

                # 代表此special不能滿足need
                # 注意!  超買則跳過此special offer.
                if min(tmp) >= 0:  # this special offer provides less then need
                    # .get check the dictionary first.
                    # for result, otherwise perform dfs.
                    total = min(total,
                                memoir.get(tuple(tmp), dfs(tmp)) + sprice)

            memoir[tuple(needs)] = total

            return total

        return dfs(needs)

    def rewrite(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """

        # 1. try them all and memoir
        # key: needs, value: price
        memoir = dict()

        def dfs(needs):

            if tuple(needs) in memoir:
                return memoir[tuple(needs)]

            # local prices
            total = sum([price[i] * n for i, n in enumerate(needs)])

            # go thourh special prices
            for s in special:
                left_needs = [n - s[i] for i, n in enumerate(needs)]
                min_needs = min(left_needs)

                if min_needs >= 0:
                    total = \
                        min(total, dfs(left_needs) + s[-1])

            # 要小心這裡!
            # 不要太早 memoir!!! 因為下一個loop 會立刻回傳非最佳解.
            memoir[tuple(needs)] = total

            return memoir[tuple(needs)]

        result = dfs(needs)

        return result


def build():

    return [3, 4], \
        [[1, 2, 3], [1, 2, 5]], \
        [2, 2]
    return [2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]


if __name__ == "__main__":
    s = Solution()
    print(s.shoppingOffers(*build()))
    print(s.rewrite(*build()))
