#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

Suppose an array sorted in ascending order is rotated
at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        if not nums:
            return

        l = 0
        r = len(nums) - 1
        # 判斷是否有rotate
        if nums[r] > nums[l]:
            return nums[l]

        while l < r:
            # 以l為pivot結果
            mid = l + (r - l)/2
            ml = nums[mid]


            if ml >= nums[0]:
                l = mid + 1
                continue

            if ml < nums[0]:
                r = mid
                continue

        return nums[l]

def build():
    return [1, 2]
    return [2, 1]
    return [3, 4, 1, 2]
    return [4, 5, 6, 7, 0, 1, 2]
    return [3, 4, 5, 1, 2]

if __name__ == "__main__":
    s = Solution()
    print(s.findMin(build()))
    #  print("---")
    #  print(s.rewrite(build()))
