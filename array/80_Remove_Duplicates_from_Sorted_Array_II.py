#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5,
with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        利用他是sorted array.
        """
        # i as 可以填入的slot index.
        i = 0

        for n in nums:
            if i < 2 or n > nums[i - 2]:  # 注意: 這裡是指 i
                nums[i] = n
                i += 1

        return i


def build():
    return [1, 2, 2, 2, 4, 5, 5, 5, 6]
    return [1, 1, 1, 2, 2, 3]


if __name__ == "__main__":

    s = Solution()
    print(s.removeDuplicates(build()))
