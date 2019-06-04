#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/subsets-ii/description/


Given a collection of integers that might contain duplicates,
nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        power_set = [[]]

        prev = float("-inf")
        prev_set = []

        for n in nums:
            if n == prev:
                subset = [item + [n] for item in prev_set]
            else:
                subset = [item + [n] for item in power_set]

            prev = n
            prev_set = subset

            power_set += subset

        return power_set


def build():
    return [1, 2, 3]
    return [1, 2, 2]


if __name__ == "__main__":

    s = Solution()
    print(s.subsetsWithDup(build()))
