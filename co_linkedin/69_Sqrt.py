#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/sqrtx/description/

Implement int sqrt(int x).
Compute and return the square root of x.
x is guaranteed to be a non-negative integer.

Example 1:
Input: 4
Output: 2


Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842...,
and since we want to return an integer, the decimal part will be truncated.
"""


class Solution(object):
    def mySqrt(self, x):
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return r

    def rewrite(self, x):
        r = x

        while r ** 2 > x:
            r = (r + x / r) / 2

        return r


def build():
    return 7


if __name__ == "__main__":

    s = Solution()
    print(s.mySqrt(build()))
    print(s.rewrite(build()))
