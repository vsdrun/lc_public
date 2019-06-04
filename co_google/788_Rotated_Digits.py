#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/rotated-digits/description/


X is a good number if after rotating each digit individually by 180 degrees,
we get a valid number that is different from X.
Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation.
0, 1, and 8 rotate to themselves;
2 and 5 rotate to each other;
6 and 9 rotate to each other,
and the rest of the numbers do
not rotate to any other number and become invalid.


Now given a positive number N, how many numbers X from 1 to N are good?


Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers,
since they remain unchanged after rotating.

注意題目!
只是單個數字本身180度
不是整個數字左右顛倒!
"""


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        s1 = set([1, 8, 0])
        s2 = set([1, 8, 0, 6, 9, 2, 5])

        def isGood(x):
            s = set([int(i) for i in str(x)])
            return s.issubset(s2) and not s.issubset(s1)

        print(isGood(69))

        return sum(isGood(i) for i in range(1, N + 1))


def build():
    return 20


if __name__ == "__main__":
    s = Solution()
    print(s.rotatedDigits(build()))
