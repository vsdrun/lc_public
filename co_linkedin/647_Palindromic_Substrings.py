#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/palindromic-substrings/description/

Given a string, your task is to count how many
palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as
different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3

Explanation: Three palindromic strings: "a", "b", "c".


Example 2:
Input: "aaa"
Output: 6

Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/
"""


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int

         “center expansion”
        """
        from __builtin__ import xrange

        N = len(s)
        ans = 0

        """
        何以要 2*N -1 ? 因為要traverse每一個點使其成為中點!

        e.g
        abc =>
        abcXXX 則 a b c可以成為中點 當 pivot / 2時!
        """

        for pivot in xrange(2 * N - 1):  # 0 1 2 3 4 => a(x)b(x)c
            center = pivot / 2
            rcenter = center + pivot % 2  # 因為n為偶數時有double center
            # 若為基數時 center 與 rcenter 相同

            while center >= 0 and rcenter < N and s[center] == s[rcenter]:
                ans += 1
                center -= 1
                rcenter += 1

        return ans


def build():
    return "aaa"


if __name__ == "__main__":

    s = Solution()
    print(s.countSubstrings(build()))
    print(s.rewrite(build()))
