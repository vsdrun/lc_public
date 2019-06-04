#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/jump-game/description/


Given an array of non-negative integers,
you are initially positioned at the first index of the array.

Each element in the array represents your
**maximum jump length**  最遠可跳幾步~~~ 這問題很不清楚.
超過 end point也算 每個node的值在 range內都算!
at that position.

Determine if you are able to reach the last index.

Example 1:
Input: [1,3,1,1,4]
Output: true

Explanation:
Jump 1 step from index 0 to 1, then 3 steps to the last index.


Example 2:
Input: [3,2,1,0,4]
Output: false

Explanation:
You will always arrive at index 3 no matter what. Its maximum
jump length is 0, which makes it impossible to reach the last index.
"""


class Solution(object):

    def canJump(self, nums):
        #  Going forwards. m tells the maximum index we can reach so far.
        m = 0

        for i, n in enumerate(nums):
            if i > m:
                return False

            m = max(m, i + n)

        return True

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """


def build():
    return [0]
    return [2, 0]
    return [2, 3, 1, 1, 4]
    return [3, 2, 1, 0, 4]


if __name__ == "__main__":

    s = Solution()
    print(s.canJump(build()))
    print(s.rewrite(build()))
