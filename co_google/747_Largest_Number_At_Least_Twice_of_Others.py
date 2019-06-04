#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/


In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice
as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer,
and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
"""


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        highest = -1
        secondHighest = -1
        highestIndex = 0

        for i, n in enumerate(nums):
            if n >= highest:
                secondHighest = highest
                highest = n
                highestIndex = i
            elif n > secondHighest:  # 重要! 是 else, if
                secondHighest = n

        if highest < secondHighest * 2:
            highestIndex = -1

        return highestIndex


def build():
    return [0, 0, 3, 2]
    return [2, 6, 1, 0]


if __name__ == "__main__":
    s = Solution()
    print(s.dominantIndex(build()))
