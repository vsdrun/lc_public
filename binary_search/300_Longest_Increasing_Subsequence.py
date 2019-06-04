#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/longest-increasing-subsequence/description/

Given an unsorted array of integers,
find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101],
therefore the length is 4.
Note that there may be more than one LIS combination,
it is only necessary for you to return the length.

Your algorithm should run in O(n^2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?


reference:
patience sort
https://en.wikipedia.org/wiki/Patience_sorting
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []

        for n in nums:
            i = 0
            j = len(result) - 1

            # 以 i 為返回的idx, 因為 i 作為pivot, 注意 corner case: [2,2,2]
            while i <= j:
                m = i + (j - i) / 2

                if result[m] >= n:  # 注意 >=
                    j = m - 1
                else:  # n < result[m]
                    i = m + 1

            if i <= len(result) - 1:
                result[i] = n
            else:
                result.append(n)

        return len(result)

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        概念很簡單...
        e.g:
        [9, 2, 5, 7, 4, 8, 1]

        [2]
        [2,5]
        [2,5,7]
        binary search for 4's location in array
        [2,4,7]
        [2,4,7,8]
        最後len == 4, 內容物不care....
        """
        import bisect as bi
        result = []

        for n in nums:

            if len(result) == 0:
                result.append(n)
            else:
                idx = bi.bisect_left(result, n)

                if idx == len(result):
                    result.append(n)
                else:
                    result[idx] = n

        return len(result)


def build():
    return [10, 9, 2, 5, 3, 7, 101, 18]
    return [5, 7, 3, 8]
    return [2, 2, 2]
    return [2, 2]
    return [9, 2, 5, 7, 4, 8, 1]


if __name__ == "__main__":

    s = Solution()
    print(s.lengthOfLIS(build()))
    print(s.rewrite(build()))
