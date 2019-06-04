#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/wiggle-sort/description/


Given an unsorted array nums,
reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
"""


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return

        from __builtin__ import xrange

        for i in xrange(1, len(nums)):
            if i % 2:
                if nums[i - 1] > nums[i]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
            else:
                if nums[i - 1] < nums[i]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        概念: 只注意一個方向的值，不要注意兩邊。
        """
        if not nums:
            return

        flip = True  # < X >, False: > X <

        for n in range(1, len(nums)):  # 注意單邊(左邊), 故len(nums)即可.
            if flip and nums[n-1] > nums[n] or \
                not flip and nums[n-1] < nums[n]:
                    nums[n-1], nums[n] = nums[n], nums[n-1]
            flip ^= True



def build():
    return [3, 5, 2, 1, 6, 4]


if __name__ == "__main__":

    s = Solution()
    b = build()
    s.wiggleSort(b)
    print(b)

    b = build()
    s.rewrite(b)
    print(b)
