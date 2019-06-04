#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/merge-sorted-array/description/


Given two sorted integer arrays nums1 and nums2,
merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space
(size that is greater or equal to m + n) to hold additional elements from
nums2. The number of elements initialized in nums1 and nums2 are
m and n respectively.

從屁股來~
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.

        由後往前填滿的概念!!! Be smart, please!!!!
        """
        l1, l2, end = m - 1, n - 1, m + n - 1

        while l1 >= 0 and l2 >= 0:
            if nums2[l2] > nums1[l1]:
                nums1[end] = nums2[l2]
                l2 -= 1
            else:
                nums1[end] = nums1[l1]
                l1 -= 1
            end -= 1

        if l1 < 0:  # if nums2 left
            nums1[:l2 + 1] = nums2[:l2 + 1]


def build():
    return [1, 2, 3, 4], 4, [3, 4, 5, 6], 4


if __name__ == "__main__":
    num1, m, num2, n = build()
    s = Solution()
    result = s.merge(num1, m, num2, n)
    print(num1)
