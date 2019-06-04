#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/number-of-1-bits/description/

Write a function that takes an unsigned integer and returns
the number of '1' bits it has (also known as the Hamming weight).

Example 1:

Input: 11
Output: 3
Explanation:
Integer 11 has binary representation 00000000000000000000000000001011

Example 2:
Input: 128
Output: 1
Explanation:
Integer 128 has binary representation 00000000000000000000000010000000
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return str(bin(n)).count('1')


def build():
    return 11
    return 128


if __name__ == "__main__":

    s = Solution()
    print(s.hammingWeight(build()))
