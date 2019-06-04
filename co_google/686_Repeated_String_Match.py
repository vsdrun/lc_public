#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/repeated-string-match/

Given two strings A and B, find the minimum number of
times A has to be repeated such that B is a substring of it.
If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”),
B is a substring of it; and B is not a substring of A repeated two times
("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        t = -(-len(B) // len(A))  # Equal to ceil(len(b) / len(a))
        return t * (B in A * t) or (t + 1) * (B in A * (t + 1)) or -1


def build():
    return "abababaaba", "aabaaba"
    return "abcd", "cdabcdab"


if __name__ == "__main__":
    a, b = build()

    s = Solution()
    result = s.repeatedStringMatch(a, b)

    print(result)
