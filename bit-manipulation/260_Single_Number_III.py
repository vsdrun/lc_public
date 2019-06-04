#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/single-number-iii/

Given an array of numbers nums, in which exactly two elements appear
only once and all the other elements appear exactly twice.

Find the two elements that appear only once.

Example:
Input:  [1,2,1,3,2,5]
Output: [3,5]

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant space complexity?

https://leetcode.com/problems/single-number-iii/discuss/68901/Sharing-explanation-of-the-solution
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Use the idea from Elements of programming, 12.12
        1. XOR the whole array, duplicated will gone, only singles left
        2. Get the least significant bit which is 1 from the above XOR,
        means that this bit is the difference between the 2 singles.
        3. Go throught the array again with the bit is 1, and XOR with the
        2 single's XOR to get the 1 single, and with this 1 single XOR with
        2 single's XOR to get another 1 single.
        負i保
        減一去
        """
        txor = 0

        for n in nums:
            txor ^= n

        # this onebit is the difference between 2 single value.
        onebit = txor & (~txor + 1)

        y = 0

        for n in nums:
            if n & onebit:
                y ^= n

        x = y ^ txor

        return [x, y]



def build():
    return [1,2,1,3,2,5]


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber(build()))
