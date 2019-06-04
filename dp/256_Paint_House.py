#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/paint-house/description/


There are a row of n houses,
each house can be painted with one of the three colors:
red, blue or green.

The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two
adjacent houses have the same color.

The cost of painting each house with a certain color is represented by
a n x 3 cost matrix.

For example, costs[0][0] is the cost of painting house 0 with color red;
costs[1][2] is the cost of painting house 1 with color green, and so on...

Find the minimum cost to paint all houses.

"""


class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        每一個current選定顏色 + 之前的其他兩個顏色哪個最便宜
        這樣構成此current的三個prices[A,B,C]
        這到最後為選每個顏色的累加值.
        所以可以return min(dp_prev)
        """
        #  之前一個的三個顏色價錢累積.
        dp_prev = [0] * 3

        for now in costs:
            dp_prev = [now[i] + min(dp_prev[:i] + dp_prev[i + 1:])
                       for i in range(3)]

        return min(dp_prev)

    def minCost_2(self, costs):
        r, b, g = 0, 0, 0

        for c in costs:
            r, b, g = min(b, g) + c[0], min(r, g) + c[1], min(r, b) + c[2]

        return min(r, b, g)


def build():
    return [[7, 6, 2], [3, 9, 3]]


if __name__ == "__main__":

    s = Solution()
    print(s.minCost(build()))
