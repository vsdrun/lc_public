#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/single-number-ii/


Given a non-empty array of integers,
every element appears three times except for one,
which appears exactly once. Find that single one.


Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?


Example 1:
Input: [2,2,3,2]
Output: 3

Example 2:
Input: [0,1,0,1,0,1,99]
Output: 99

https://leetcode.com/problems/single-number-ii/discuss/43332/My-own-explanation-of-bit-manipulation-method-might-be-easier-to-understand
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        One+ = (One ^ B) & (~Two)
        Two+ = (~One+) & (Two ^ B)
        """

        ones = 0
        twos = 0

        for c in nums:
            ones = (ones ^ c) & ~ twos
            twos= (twos ^ c) & ~ ones

        return ones




def build():
    return [2,2,3,2]


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber(build()))
