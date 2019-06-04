#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/house-robber/description/

You are a professional robber planning to rob houses along a street.

Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have
security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money
of each house,
determine the maximum amount of money you can rob
tonight without alerting the police.
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        f(0) = nums[0]
        f(1) = max(num[0], num[1])
        f(k) = max( f(k-2) + nums[k], f(k-1) )
        """

        last, now = 0, 0

        for i in nums:
            last, now = now, max(last + i, now)

        return now

    def wrong(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        O(n)
        不是算奇數偶數和...
        """
        from __builtin__ import xrange
        even_sum = odd_sum = 0

        for i in xrange(0, len(nums), 2):
            even_sum += nums[i]

        for i in xrange(1, len(nums), 2):
            odd_sum += nums[i]

        return max(even_sum, odd_sum)

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        O(n)

        Consider, the node's value can be counted with previous valid value.

        i.e Any node's value before the previous node.

        and if this node has to be counted? Because , it might not

        produce max value.
        """

        prev = current = 0

        for n in nums:
            prev, current = current, max(n + prev, current)

        return current


def build():
    return [1]
    return [2, 1, 1, 2]
    return [4, 1, 2, 9, 10]
    return [3, 1, 9, 7, 5]


if __name__ == "__main__":
    s = Solution()
    print(s.rob(build()))
    print(s.rewrite(build()))
