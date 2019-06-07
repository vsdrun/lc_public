#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/maximum-subarray/description/


Given an integer array nums,
find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach,
which is more subtle.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        連續累加概念。
        將最小的複數減去 其後的便是連續最大和。

        注意! 仍要紀錄最大值! 因為即使和都是正數
        仍有最大和的正數!
        """
        from __builtin__ import xrange

        mmin = 0
        tt = 0

        mmax = float("-inf")

        for i in xrange(len(nums)):
            tt += nums[i]
            mmax = max(mmax, tt - mmin)
            mmin = min(mmin, tt)

        return mmax

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        連續累加概念。
        將最小的複數減去 其後的便是連續最大和。
        注意! 仍要紀錄最大值! 因為即使和都是正數
        仍有最大和的正數!
        """
        maxsum = float("-inf")
        minsum = 0
        localSum = 0

        for n in nums:
            localSum += n
            maxsum = max(maxsum, localSum - minsum)
            minsum = min(minsum, localSum)

        return maxsum


def build():
    return [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    return [-2, -1]


if __name__ == "__main__":

    s = Solution()
    print(s.maxSubArray(build()))
    print(s.rewrite(build()))
