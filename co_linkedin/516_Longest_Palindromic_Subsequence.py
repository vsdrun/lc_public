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

        Idea:
        dp[i][j] = longest palindrome subsequence of s[i to j].
        If s[i] == s[j], dp[i][j] = 2 + dp[i+1][j - 1]
        Else, dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        """
        n = len(s)
        dp = [1] * n

        for j in range(1, len(s)):
            pre = dp[j]
            print("pre: {}".format(pre))

            # 每次均重新計算DP,
            # 以前一個dp[i]存目前最長的結果
            for i in range(j-1, -1, -1):
                tmp = dp[i]

                if s[i] == s[j]:
                    dp[i] = 2 + pre if i + 1 <= j - 1 else 2
                else:
                    dp[i] = max(dp[i + 1], dp[i])

                pre = tmp

        return dp[0]


def build():
    return "bbbab"


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindromeSubseq(build()))
