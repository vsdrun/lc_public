#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/add-digits/description/


Given a non-negative integer num,
repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2.
Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        """
        Idea:
        所有數字的和 % 9 == 最後的一位數字.
        因為 e.g 6 + 3
        1 1 1 1 1 1,  1 1 1
        """

        if not num % 9:
            if not num:
                return num
            else:
                return 9

        return num % 9


def build():
    return 18


if __name__ == "__main__":

    s = Solution()
    print(s.addDigits(build()))
