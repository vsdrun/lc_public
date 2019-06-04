#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/rotate-string/description/

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost
character to the rightmost position.

For example, if A = 'abcde', then it will be 'bcdea' after one shift on A.
Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.
"""


class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        return B in A*2


def build():
    return 'abcde', 'cdeab'

if __name__ == "__main__":
    print(Solution().rotateString(*build()))
