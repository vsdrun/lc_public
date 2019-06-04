#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Given a set of distinct positive integers, find the largest
subset such that every pair (Si, Sj) of elements in this
subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:
nums: [1,2,3]
Result: [1,2] (of course, [1,3] will also be ok)


Example 2:
nums: [1,2,4,8]
Result: [1,2,4,8]
"""


class Solution(object):

    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        if len(nums) == 1:
            return nums

        nums.sort()
        maxSet = set()
        dp = {}
        one = False

        if nums[0] == 1:
            maxSet.add(1)
            nums = nums[1:]
            one = True

        for i, n in enumerate(nums):
            dp[i] = set()
            dp[i].add(n)

            if one:
                dp[i].add(1)

            localMax = set(dp[i])

            for j in xrange(i - 1, -1, -1):
                partial = n % max(dp[j])

                if partial == 0:
                    dp[i].update([k for k in dp[j]])
                if len(dp[i]) > len(localMax):
                    localMax = set(dp[i])

            if len(dp[i]) > len(maxSet):
                maxSet = dp[i]

        r = list(maxSet)
        r.sort()
        return r


def build_input():
    #  return [1, 2, 4, 8, 12]
    #  return [24, 12, 30, 1]
    #  return [1, 2000000000]
    #  return [4, 8, 10, 240]
    return [2, 4, 6, 12]


if __name__ == "__main__":
    n = build_input()

    s = Solution()
    result = s.largestDivisibleSubset(n)

    # [1, 2, 4, 8]
    print(result)
