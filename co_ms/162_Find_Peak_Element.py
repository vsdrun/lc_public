#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-peak-element/

A peak element is an element that is
greater than its neighbors.

Given an input array where num[i] ≠ num[i+1],
find a peak element and return its index.

The array may contain multiple peaks,
in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1],
3 is a peak element and your function should

return the index number 2.
"""


class Solution(object):

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        forward list search
        """
        if len(nums) < 2:
            return 0

        for i in xrange(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return i - 1
        return len(nums) - 1

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        也可思考 log(n) solution!
        """
        from __builtin__ import xrange

        peak = -1

        for i in xrange(1, len(nums)):
            if peak == -1 and nums[i] < nums[i - 1]:
                peak = i - 1

        return peak if peak != -1 else len(nums) - 1


def build():
    return [3, 2, 1]
    return [2, 1]
    return [1, 2, 3, 1]
    return [1, 2]
    return [1]


if __name__ == "__main__":
    s = Solution()
    result = s.findPeakElement(build())
    print(result)
    result = s.rewrite(build())
    print(result)
