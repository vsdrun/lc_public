#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/3sum-closest/

Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            # 前後夾擠
            j = i + 1
            k = len(nums) - 1

            while j < k:
                csum = nums[i] + nums[j]  + nums[k]

                if csum == target:
                    return csum

                if abs(csum - target) < abs(result - target):
                    result = csum

                if csum > target:
                    k -= 1
                else:
                    j += 1

        return result

def build():
    return  [-1, 2, 1, -4], 1


if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest(*build()))
