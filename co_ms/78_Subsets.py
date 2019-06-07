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
        using bitmap, slow
        and operation: -i 保, -1 去
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
    print(s.subsets(build()))
    print(s.rewrite(build()))
