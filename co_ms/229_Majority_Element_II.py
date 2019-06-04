#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/majority-element-ii/description/

Given an integer array of size n,
find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:
Input: [3,2,3]
Output: [3]

Example 2:
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        https://leetcode.com/problems/majority-element-ii/discuss/63502/6-lines-general-case-O(N)-time-and-O(k)-space
        """
        import collections as cc

        ctr = cc.Counter()

        for n in nums:
            ctr[n] += 1

            if len(ctr) == 3:
                ctr -= cc.Counter(set(ctr))

        return [n for n in ctr if nums.count(n) > len(nums)/3]

def build():
    return [1,2,2,4,5]
    return [1,2,2,3,4,5]
    return [1,1,1,3,3,2,2,2]


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement(build()))
