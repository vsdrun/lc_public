#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/guess-number-higher-or-lower/description/

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results
(-1, 1, or 0):

-1 : My number is higher
 1 : My number is lower
 0 : Congrats! You got it!

Example:
n = 10, I pick 6.

Return 6.
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0


def guess(num):
    answer = 7

    if num < answer:
        return 1
    if num > answer:
        return -1
    if num == answer:
        return 0


class Solution(object):

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n

        while lo < hi:
            mid = (lo + hi) / 2

            if guess(mid) == 1:
                lo = mid + 1
            else:
                hi = mid
        return lo


def build_input():
    pass


if __name__ == "__main__":
    n = build_input()

    s = Solution()
    result = s.guessNumber(10)

    print(result)
