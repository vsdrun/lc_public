#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/


Given an array of n positive integers and a positive integer,
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

    def rewrite(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        Better!
        1. nums內的數為 > 0! 這很重要!!
        """
        mlength = float('inf')
        total = 0
        r_idx = 0

        for idx, n in enumerate(nums):
            total += n

            # corner case, 前面的為小數目 此一數超大.
            while total >= s:
                print(idx)
                print(r_idx)
                mlength = min(mlength, idx - r_idx)
                total -= nums[r_idx]
                r_idx += 1

        return mlength + 1 if mlength != float('inf') else 0


def build():
    return 11, [10, 1]
    return 7, [2, 3, 1, 1, 4, 3]
    return 15, [1, 2, 3, 4, 5]


if __name__ == "__main__":

    s = Solution()
    print(s.minSubArrayLen_linear(*build()))
    print(s.minSubArrayLen(*build()))
    print(s.rewrite(*build()))
