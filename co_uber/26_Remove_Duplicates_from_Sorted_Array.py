#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Given a sorted array, remove the duplicates in-place such that
each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.

Example:
Given nums = [1,1,2],

Your function should return length = 2,
with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the new length.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        midx = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[midx]:
                continue

            midx += 1
            nums[midx] = nums[i]

        return midx + 1 if nums else 0

def build():
    return [1, 1, 2, 2, 3, 3, 7, 8, 9, 9]
    return []
    return [1]
    return [1,1,2]
    return [1, 2, 3, 4]


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates(build()))
