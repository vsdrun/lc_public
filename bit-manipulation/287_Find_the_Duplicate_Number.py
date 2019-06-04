#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-the-duplicate-number/description/

Given an array nums containing n + 1 integers where each integer is
between 1 and n (inclusive),
prove that at least one duplicate number must exist.
Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Using xor.
        """
        xor = 0

        for n in nums:
            xor ^= n

        for i in range(1, len(nums) + 1):
            xor ^= i

        last = xor & -xor

        x = y = 0

        for i in range(len(nums)):
            if last & nums[i]:
                x ^= nums[i]
            else:
                y ^= nums[i]

        for i in range(1, len(nums) + 1):
            if i & last:
                x ^= i
            else:
                y ^= i

        return x if x in nums else y

def build():
    return [3,1,3,4,2]
    return [1,3,4,2,2]


if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate(build()))
