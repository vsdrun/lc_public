#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/longest-palindromic-subsequence/description/


Given a string s, find the longest palindromic subsequence's length in s.
You may assume that the maximum length of s is 1000.



Example 1:
Input:
"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".


Example 2:
Input:

"cbbd"
Output:
2
"""


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        idea:
        if dp[i]==dp[j]
        """
        dp = [0] * len(s)


def build():
    return "bbbab"


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindromeSubseq(build()))
