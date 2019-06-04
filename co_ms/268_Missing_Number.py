#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/missing-number/description/

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

Example 1

Input: [3,0,1]
Output: 2
Example 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from __builtin__ import xrange

        n = len(nums) + 1

        total_xor = 0

        for num in xrange(1, n):
            total_xor ^= num

        local_xor = nums[0]

        for i in xrange(1, len(nums)):
            local_xor ^= nums[i]

        result = total_xor ^ local_xor
        return result

    def youshouldbesmart(self, nums):
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)


def build():
    return [9, 6, 4, 2, 3, 5, 7, 0, 1]


if __name__ == "__main__":

    s = Solution()
    result = s.missingNumber(build())

    print(result)
