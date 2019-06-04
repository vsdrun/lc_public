#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/move-zeroes/description/

Given an array nums, write a function to move all 0's to
the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12],
after calling your function, nums should be [1, 3, 12, 0, 0].


Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0  # records the position of "0"

        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        zeroIdx = 0

        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[zeroIdx], nums[idx] = nums[idx], nums[zeroIdx]
                zeroIdx += 1


def build():
    return [0, 1, 0, 3, 12]


if __name__ == "__main__":

    s = Solution()
    nums = build()
    result = s.moveZeroes(nums)
    print(nums)

    nums = build()
    result = s.rewrite(nums)
    print(nums)
