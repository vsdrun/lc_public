#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

Given an array of integers,

1 ≤ a[i] ≤ n (n = size of array),

some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""


class Solution(object):

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        # 以正負來判斷是否已經有重複.
        for x in nums:
            # -1 因為 array index starts with 0
            if nums[abs(x) - 1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
                print(nums)

        return res


def build():
    return [4, 3, 2, 7, 8, 2, 3, 1]


if __name__ == "__main__":
    n = build()
    s = Solution()
    r = s.findDuplicates(n)
    print(r)
