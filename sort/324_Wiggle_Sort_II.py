#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] >
# nums[2] < nums[3]...

"""
https://leetcode.com/problems/wiggle-sort-ii/description/

Given an unsorted array nums,
reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""


class Solution(object):

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        1. 先sort
        2. 分成兩半，小的一群 大的一群
        3. 一次次由小的拿一個 大的拿一個 小的拿一個...
        4. a < b > c < d.. 因為大的一群永遠比小的大...
        """
        nums.sort()

        half = len(nums[::2])

        nums[::2], nums[1::2] = nums[:half][::-1], nums[half::][::-1]


def build_input():
    #  result = [3, 5, 5, 5, 5, 2, 6]
    #  result = [100]
    #  result = [0, 1, 1, 4, 4, 5, 6]
    #  result = [11, 15]
    result = [1, 3, 4]
    return result


if __name__ == "__main__":
    input = build_input()

    s = Solution()
    s.wiggleSort(input)

    print(input)
