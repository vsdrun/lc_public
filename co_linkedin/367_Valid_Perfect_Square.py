#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/valid-perfect-square/description/

Given a positive integer num,
write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        背起來....
        """

        if num == 0 or num == 1:
            return True
        if num < 0:
            return False

        r = num

        while r ** 2 > num:
            r = (r + num / r) / 2

        return r ** 2 == num


def build():
    return 17


if __name__ == "__main__":
    s = Solution()
    print(s.isPerfectSquare(build()))
