#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/house-robber-ii/description/


You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.


Meanwhile,
adjacent houses have security system connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.


Given a list of non-negative integers representing the amount of money of
each house,
determine the maximum amount of money you can rob tonight
without alerting the police.


Example 1:
Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3
(money = 2), because they are adjacent houses.


Example 2:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        概念: 由198來.
        先由前往後 rob, 但是最後一個不能rob, 因為cycle.
        再由後往前 rob, 但是第一個不能rob, 因為cycle.
        """

        if len(nums) == 1:
            return nums[0]

        if not nums:
            return 0

        from __builtin__ import xrange

        prev = curr = 0

        for i in xrange(len(nums) - 1):
            prev, curr = curr, max(nums[i] + prev, curr)

        max_forward = curr

        # ----分隔----

        prev = curr = 0

        for i in xrange(len(nums) - 1, 0, -1):
            prev, curr = curr, max(nums[i] + prev, curr)

        max_backward = curr

        return max(max_forward, max_backward)


def build():
    return [1]
    return [1, 3, 1, 3, 100]
    return [2, 3, 2]
    return [1, 2, 3, 1]


if __name__ == "__main__":

    s = Solution()
    result = s.rob(build())
    print(result)
