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

1. continuous sum, 累積和
2. O(n)
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

        可以處理負數和!
        """

        for x in nums:
            sum += x
            ans += count[sum - k]
            count[sum] += 1  # += because input array could have value 0.

        return ans

    def rewrite(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        4
        1, 2, 2, 5
        要能處理負數!
        """
        from collections import Counter as cc
        dmap = cc()
        dmap[0] = 1

        summ = 0
        cnt = 0

        for n in nums:
            summ += n
            cnt += dmap[summ - k]
            dmap[summ] += 1

        return cnt



def build():
    return [1,2,3], 3
    return [1], 0
    return [1, 1, 1, 2, 3, 4, 6, 7, 9], 3


if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum(*build()))
    print(s.rewrite(*build()))
