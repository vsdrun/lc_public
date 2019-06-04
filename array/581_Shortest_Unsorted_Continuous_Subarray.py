#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/


Given an integer array, you need to find one continuous subarray that
if you only sort this subarray in ascending order,
then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9]
in ascending order to make the whole array sorted in ascending order.
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        先 sort 再看差異!


        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)
        """
        snums = sorted(nums)

        same = [a == b for (a, b) in zip(snums, nums)]

        return 0 if all(same) else len(nums) - same.index(False) - \
            same[::-1].index(False)


def build():
    return [1, 3, 2, 2, 2]  # 4 [1, 2, 2, 2, 3] [T, F, T, T, F]
    return [1, 3, 2, 3, 3]  # [ 1, 2, 3, 3, 3] [T, F, F, T, T]

    # [2, 4, 6, 8, 9, 10, 15] , [T, F, F, T, F,  F, T]
    return [2, 6, 4, 8, 10, 9, 15]
    return [1, 2, 3, 4]  # 0
    return [2, 6, 4, 8, 10, 15]


if __name__ == "__main__":
    s = Solution()
    print(s.findUnsortedSubarray(build()))
