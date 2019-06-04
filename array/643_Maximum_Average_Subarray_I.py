#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/maximum-average-subarray-i/description/

Given an array consisting of n integers,
find the contiguous subarray of given length k that has the maximum
average value.
And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) < k:
            return 0

        i = 0
        total = 0
        avg = float("-inf")

        while i < len(nums):
            total += nums[i]

            if i == (k - 1):
                avg = max(avg, total)

            if i >= k:
                total -= nums[i - k]
                avg = max(avg, total)

            i += 1

        return float(avg) / k


def build():
    return [1, 12, -5, -6, 50, 3], 4


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxAverage(*build()))
