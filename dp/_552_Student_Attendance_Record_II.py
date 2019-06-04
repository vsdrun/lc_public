#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a positive integer n, return the number of all possible attendance
records with length n, which will be regarded as rewardable. The answer
may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following
three characters:

'A': Absent.
'L': Late.
'P': Present.

A record is regarded as rewardable if it doesn't contain more than one 'A'
(absent) or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times.
"""


class Solution(object):

    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """


def build_input():
    return ["10", "0001", "111001", "1", "0"], 5, 3


if __name__ == "__main__":
    n = build_input()

    s = Solution()
    result = s.checkRecord(n)

    print(result)
