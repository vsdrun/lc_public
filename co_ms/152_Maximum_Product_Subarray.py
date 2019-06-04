#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/maximum-product-subarray/

Find the contiguous subarray within an array
(containing at least one number) which has the largest product.

For example,

given the array [3, -1, -2, 2, 3, -2, 4]
the contiguous subarray [2,3]
has the largest product = 6.


DP.
一個傳一個...
傳 Big and Small.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxim = big = small = nums[0]

        for n in nums[1:]:
            l_big = max(n, n * big, n * small)

            l_small = min(n, n * big, n * small)

            big = l_big  # 傳遞至下一個loop

            small = l_small  # 傳遞至下一個loop

            maxim = max(maxim, big)  # 存目前最大

        return maxim


def build():
    return [2, 3, -2, 4]


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct(build()))
