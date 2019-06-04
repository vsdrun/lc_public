#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/max-consecutive-ones/description/


Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from __builtin__ import xrange

        mx = 0

        curr = 0

        for i in xrange(len(nums)):
            if nums[i] == 1:
                curr += 1
                mx = max(mx, curr)
            else:
                curr = 0
        return mx


def build():
    return [1, 1, 0, 1, 0, 1]


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxConsecutiveOnes(build()))
