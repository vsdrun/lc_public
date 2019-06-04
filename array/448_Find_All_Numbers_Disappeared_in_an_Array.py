#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/


Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the
returned list does not count as extra space.

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""


class Solution(object):

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from __builtin__ import xrange
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
        print(nums)
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


def build():
    return [4, 3, 2, 7, 8, 2, 3, 1]


if __name__ == "__main__":
    n = build()
    s = Solution()
    r = s.findDisappearedNumbers(n)
    print(r)
