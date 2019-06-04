#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/intersection-of-two-arrays/description/

Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:
Each element in the result must be unique.
The result can be in any order.
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a, b = (nums1, nums2) if len(nums1) >= len(nums2) else (nums2, nums1)

        result = set()

        for n in a:
            if n in b:
                result.add(n)

        return list(result)

    def rewrite(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1s = set(nums1)
        n2s = set(nums2)

        return list(n1s & n2s)


def build():
    return [1, 2, 2, 1], [2, 2]

if __name__ == "__main__":
    s = Solution()
    print(s.intersection(*build()))
    print(s.rewrite(*build()))
