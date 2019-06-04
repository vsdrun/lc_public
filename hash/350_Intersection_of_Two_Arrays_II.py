#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk,
and the memory is limited such that you cannot load all elements into the memory at once?
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter as CC

        nums1, nums2 = (nums1, nums2) if len(nums1) >= len(nums2) else \
            (nums2, nums1)

        n2dmap = CC(nums2)
        result = []

        for n1 in nums1:
            if n1 in n2dmap:
                result.append(n1)
                n2dmap.subtract([n1])

                if n2dmap[n1] == 0:
                    n2dmap.pop(n1)

        return result

def build():
    return [4,9,5], [9,4,9,8,4]


if __name__ == "__main__":
    s = Solution()
    print(s.intersect(*build()))
