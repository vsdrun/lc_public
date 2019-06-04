#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/summary-ranges/description/

Given a sorted integer array without duplicates,
return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
"""


class Solution(object):

    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []

        for n in nums:
            # 有趣的條件設定...
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],

            # always add after 1, why? because we are getting range:
            # [1, n]
            ranges[-1][1:] = n,

        return ['->'.join(map(str, r)) for r in ranges]


def build():
    return [0, 1, 2, 4, 5, 7]


if __name__ == "__main__":
    nums = build()

    s = Solution()
    result = s.summaryRanges(nums)

    # ["0->2","4->5","7"]
    print(result)
