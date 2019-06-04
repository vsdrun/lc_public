#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/two-sum/description/

Given an array of integers,
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        gdict = {}

        for i, n in enumerate(nums):
            remain = target - n

            if remain in gdict:
                return [gdict[remain], i]
            gdict[n] = i

        return []

    def rewrite(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dmap = dict()

        for idx, n in enumerate(nums):
            if target - n in dmap:
                return [dmap[target - n], idx]

            dmap[n] = idx

        return []

def build():
    return [7, 1, 5, 3, 6, 4], 11


if __name__ == "__main__":

    s = Solution()
    print(s.twoSum(*build()))
    print(s.rewrite(*build()))
