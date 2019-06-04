#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


class Solution(object):
    def searchRange(self, nums, target):
        import bisect as bi

        lidx = bi.bisect_left(nums, target)
        if lidx >= len(nums) or nums[lidx] != target:
            return [-1, -1]

        ridx = bi.bisect_right(nums, target)

        return [lidx, ridx - 1] if ridx - 1 != lidx else [lidx, lidx]


def build():
    return [5, 7, 7, 8, 8, 10], 8
    return [5, 7, 7, 8], 5
    return [2, 2], 3
    return [5, 7, 7, 8], 8


if __name__ == "__main__":
    s = Solution()
    print(s.searchRange(*build()))
