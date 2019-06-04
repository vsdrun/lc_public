#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/subsets/description/

Given a set of distinct integers, nums,
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import math as m

        length = len(nums)
        bitLen = 1 << length

        result = []

        while bitLen:
            tmp_result = []
            bitLen -= 1
            current_bit = bitLen

            while current_bit:
                idx = current_bit & (-current_bit)
                tmp_result.append(nums[int(m.log(idx, 2))])
                current_bit = current_bit & (current_bit - 1)

            result.append(tmp_result)

        return result

    def subsets_2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Simple and Smart!
        """
        power_set = [[]]

        for num in sorted(nums):
            power_set += [item + [num] for item in power_set]

        return power_set

    def subsets_3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        power_set = [[]]

        for num in nums:
            tmp_r = [item + [num] for item in power_set]
            print(tmp_r)
            power_set += tmp_r
            print(power_set)
            print("\n")

        return power_set

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = [[]]

        for n in nums:
            tmp = []

            for r in result:
                tmp.append(r + [n])

            result.extend(tmp)
        return result

def build():
    return [1, 2, 3]


if __name__ == "__main__":
    s = Solution()
    print(s.subsets_3(build()))
    print(s.rewrite(build()))
