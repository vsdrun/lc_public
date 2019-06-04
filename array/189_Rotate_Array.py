#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/rotate-array/description/


Given an array, rotate the array to the right by k steps,
where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]

Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]

        """
        from __builtin__ import xrange
        ll = len(nums)

        k = k % ll

        for _ in xrange(k):
            nums[:1], nums[1:] = nums[-1:], nums[: -1]
        """


def build():
    return [-1, -100, 3, 99, 7, 8, 11], 3


if __name__ == "__main__":
    s = Solution()
    b = build()
    s.rotate(*b)
    print(b[0])
