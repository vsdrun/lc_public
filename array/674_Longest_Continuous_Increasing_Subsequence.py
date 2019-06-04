#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

Given an unsorted array of integers,
find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation:
The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence,
it's not a continuous one where 5 and 7 are separated by 4.


Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation:
The longest continuous increasing subsequence is [2], its length is 1.
不是patience sort, 因為是continious sub array
"""


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        cnt = 1
        lcnt = 1

        for idx in xrange(1, len(nums)):
            if nums[idx] > nums[idx - 1]:
                lcnt += 1
                cnt = max(cnt, lcnt)
            else:
                lcnt = 1

        return cnt


def build():
    return [1,7,2,9,5]
    return []
    return [1, 3, 5, 7, 9, 11, 12, 3, 7, 9, 10, 12]
    return [2, 2, 2, 2, 2]


if __name__ == "__main__":

    s = Solution()
    print(s.findLengthOfLCIS(build()))
