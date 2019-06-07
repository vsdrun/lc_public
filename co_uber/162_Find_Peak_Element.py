#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/find-peak-element/

A peak element is an element that is
greater than its neighbors.

Given an input array where num[i] ≠ num[i+1],
find a peak element and return its index.

The array may contain multiple peaks,
** Thus it's easy...
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


def build_input():
    return [1, 2]
    return [1]
    return [1, 2, 3, 1]


if __name__ == "__main__":
    m = build_input()

    s = Solution()
    result = s.findPeakElement(m)

    print(result)
