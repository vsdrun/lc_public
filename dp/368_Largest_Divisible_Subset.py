#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/largest-divisible-subset/description/

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

思考:
    一數n 若能被 m整除，則任何能整除m的數也能整除n.


My S[x] is the largest subset with x as the largest element,
i.e., the subset of all divisors of x in the input.
With S[-1] = emptyset as useful base case.
Since divisibility is transitive, a multiple x of some divisor d
is also a multiple of all elements in S[d],
so it's not necessary to explicitly test divisibility of x by all
elements in S[d].
Testing x % d suffices.

While storing entire subsets isn't super efficient, it's also not that bad. To
extend a subset, the new element must be divisible by all elements in it,
meaning it must be at least twice as large as the largest element in it.
So with the 31-bit integers we have here,
the largest possible set has size 31
(containing all powers of 2).

def largestDivisibleSubset(self, nums):
    S = {-1: set()}

    for x in sorted(nums):
        S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}

    return list(max(S.values(), key=len))
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

        # 由小至大
        nums.sort()

        # 以 n 為 key, value為set of
        dp = {}
        globalMaxSet = []

        def maxSet(sl, n):
            # sl: list of number which is smaller then n.
            maxLocal = set()

            for s in sl:
                # n 可以被 s 除盡.
                if not (n % s):
                    maxLocal = dp[s] if len(dp[s]) > len(maxLocal) else maxLocal

            return maxLocal

        for i, n in enumerate(nums):
            dp[n] = set()
            dp[n].add(n)

            # 重點於此
            dp[n].update(maxSet(nums[:i], n))

            if len(dp[n]) > len(globalMaxSet):
                globalMaxSet = list(dp[n])

        globalMaxSet.sort()
        return globalMaxSet


def build_input():
    #  return [1, 2, 4, 8, 12]
    return [24, 12, 30, 1]
    #  return [1, 2000000000]
    #  return [4, 8, 10, 240]
    return [2, 4, 6, 12]


if __name__ == "__main__":
    n = build_input()

    s = Solution()
    result = s.largestDivisibleSubset(n)

    # [1, 2, 4, 8]
    print(result)
