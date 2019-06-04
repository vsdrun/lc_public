#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/


Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
"""


class Solution(object):
    def minSubArrayLen_linear(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        Better!
        1. nums內的數為 > 0! 這很重要!!
        """
        total = 0
        s_idx = 0
        lg = float("inf")

        for i, n in enumerate(nums):
            total += n

            while total >= s:
                lg = min(i - s_idx, lg)
                total -= nums[s_idx]
                s_idx += 1

        return 0 if lg == float("inf") else lg + 1

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        import bisect as bi

        s_array = [(0, -1)]  # num, idx
        total = 0
        lg = float("inf")

        for i, n in enumerate(nums):
            total += n
            # 找 <= diff 的 減去, 也就是 < (diff + 1)
            diff = total - s

            if diff >= 0:
                idx = bi.bisect_left(s_array, (diff + 1, float("-inf")))
                idx = s_array[idx - 1][1] + 1
                lg = min(lg, i - idx)

            s_array += (total, i),

        return 0 if lg == float("inf") else lg + 1


def build():
    return 15, [1, 2, 3, 4, 5]
    return 7, [2, 3, 1, 1, 4, 3]


if __name__ == "__main__":

    s = Solution()
    #  print(s.minSubArrayLen_linear(*build()))
    print(s.minSubArrayLen(*build()))
