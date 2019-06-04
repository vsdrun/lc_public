#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/create-maximum-number/description/

Given two arrays of length m and n with digits 0-9 representing two
numbers.

Create the maximum number of length k <= m + n from digits of
the two.

The relative order of the digits from the same array must be
preserved.

Return an array of the k digits.
You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]
"""


class Solution(object):

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def prep(nums, k):
            if len(nums) == k:
                return nums[:]

            drop = len(nums) - k
            out = []

            for num in nums:
                while drop and out and out[-1] < num:
                    # dump the 'drop' number and preserve the largest.
                    out.pop()
                    drop -= 1
                out.append(num)

            # In case input list is : [5,4,3] and we only need 2
            # of them.
            result = out[:k]
            return result

        def merge(a, b):
            return [max(a, b).pop(0) for _ in a + b]

        return max(merge(prep(nums1, i), prep(nums2, k - i))
                   for i in range(k + 1)
                   if i <= len(nums1) and k - i <= len(nums2))


def build_input():
    num1 = [8, 6, 9]
    num2 = [1, 7, 5]
    return num1, num2


if __name__ == "__main__":
    n1, n2 = build_input()

    s = Solution()
    result = s.maxNumber(n1, n2, 3)

    print(result)
