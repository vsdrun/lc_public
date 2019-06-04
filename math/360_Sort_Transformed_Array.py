#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/sort-transformed-array/

Given a sorted array of integers nums and integer values a, b and c.
Apply a quadratic function of the form f(x) = ax^2 + bx + c
to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example 1:
Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]

Example 2:
Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
"""


class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        import bisect as bi

        result = []

        for x in nums:
            res = a*(x**2) + b*x + c
            bi.insort_left(result, res)

        return result

def build():
    return [-4,-2,2,4], 1, 3, 5


if __name__ == "__main__":
    s = Solution()
    print(s.sortTransformedArray(*build()))
