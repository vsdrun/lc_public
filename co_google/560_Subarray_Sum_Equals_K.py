#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/subarray-sum-equals-k/description/


Given an array of integers and an integer k,
you need to find the total number of continuous
subarrays whose sum equals to k.


Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
"""


class Solution(object):

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import collections

        count = collections.Counter()
        count[0] = 1

        print("count: {0}".format(count))

        ans = sum = 0
        """
        概念:
        目前的和 減去 k 代表 剩下的數之前的list和有辦法表示嗎?
        若有辦法表示代表: 現在這個list可以成為一個表示。
        """

        for x in nums:
            sum += x
            ans += count[sum - k]
            count[sum] += 1  # += because input array could have value 0.

        return ans


def build():
    return [1, 1, 1, 2, 3, 4, 6, 7, 9]


if __name__ == "__main__":
    n = build()
    s = Solution()
    r = s.subarraySum(n, 3)
    print(r)
