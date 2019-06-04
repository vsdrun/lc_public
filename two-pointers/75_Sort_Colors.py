#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/sort-colors/description/


Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.


Here, we will use the integers 0, 1, and 2 to represent the color
red, white, and blue respectively.


Note:
You are not suppose to use the library's sort function for this problem.
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        smallIdx = movingIdx = 0
        largeIdx= len(nums)

        while movingIdx < largeIdx:
            if nums[movingIdx] < 1:
                nums[smallIdx], nums[movingIdx] = nums[movingIdx], nums[smallIdx]
                smallIdx += 1
            elif nums[movingIdx] > 1:
                largeIdx -= 1
                nums[movingIdx], nums[largeIdx] = nums[largeIdx], nums[movingIdx]
                continue


            movingIdx += 1



def build():
    return [1, 2, 0] # 1, 0, 2 |
    return [2, 1, 2, 1, 0, 1, 2]  # [0,1,1,1,2,2,2]
    return [2, 0, 1] # [1, 0, 2], [0, 1, 2]
    return [1, 0]


if __name__ == "__main__":
    nums = build()
    s = Solution()
    nums = build()
    s.sortColors(nums)
    print(nums)
    print("----")
