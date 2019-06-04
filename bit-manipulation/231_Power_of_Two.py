#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/power-of-two/

Given an integer, write a function to determine if it is a power of two.
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        Only one 1 in n in binary format.
        i.e removing the last 1 should be 0.
        """
        if not n:
            return False

        if n & (n - 1):
            return False
        else:
            return True


def build_input():
    result = 5
    return result


if __name__ == "__main__":
    input = build_input()

    s = Solution()
    result = s.isPowerOfTwo(input)

    print(result)
