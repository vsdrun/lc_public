#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

A conveyor belt has packages that must be shipped from one port
to another within D days.

The i-th package on the conveyor belt has a weight of weights[i].
Each day, we load the ship with packages on the conveyor belt
(in the order given by weights).
We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the
packages on the conveyor belt being shipped within D days.


Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation:
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a
ship of capacity 14 and splitting the packages into parts like
(2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.


Example 2:
Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation:
A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4


Example 3:
Input: weights = [1,2,3,1,1], D = 4
8 / 4 = 2
[1, 3, 6, 7, 8]
 1  2  3  1  1

Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

Note:

1 <= D <= weights.length <= 50000
1 <= weights[i] <= 500
"""

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
        """

        left, right = max(weights), sum(weights)

        # 10 < 55, 也就是，最小必須為10, 不然沒有船可以載
        while left < right:
            mid = (left + right) / 2
            need = 1  # 需要的天數
            cur = 0  # 累積重量 per 天

            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w

            if need > D:
                left = mid + 1
            else:
                right = mid

        return left


def build():
    """
Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
    11 * 10 / 2 = 55
    55/5 = 11 kg/day
    """
    return [1,2,3,4,5,6,7,8,9,10], 5

if __name__ == "__main__":
    s = Solution()
    print(s.shipWithinDays(*build()))
