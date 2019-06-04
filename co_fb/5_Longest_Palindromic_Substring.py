#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.


Example 2:
Input: "cbbd"
Output: "bb"
1. 1個奇 其他偶
2. 前後夾擠
3. 由最長開始前後長 判斷.
https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        此解用DP.
        """
        if len(s) == 0:
            return ""
        elif len(s) == 1:
            return s

        table = [[False]*len(s) for _ in range(len(s))]
        start = 0
        end = 0

        # 中間的char
        for i in range(len(s)):
            table[i][i] = True

        print("-----\n")
        print("table: {}".format(table))
        print("-----\n")

        for i in range(len(s)-1):
            # 處理重複的值
            if s[i] == s[i+1]:
                table[i][i+1] = True
                start = i
                end = i+1
            else:
                table[i][i+1] = False

        print("start: {} end: {}".format(start, end))

        # caaac len(s) == 5
        for l in range(3, len(s)+1):
            for i in range(len(s)-l+1):
                j = i+l-1

                print("i: {}".format(i))
                if s[i] == s[j] and table[i+1][j-1]:  # 往內夾擠
                    table[i][j] = True
                    start = i
                    end = j
                else:
                    table[i][j] = False

        print("start: {} end: {}".format(start, end))
        return s[start:end+1]

    def rewrite(self, s):
        """
        :type s: str
        :rtype: str
        此解用DP.
        """


def build():
    return "aaaa"
    return "bbbad"
    return "babad"


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome(build()))
    print(s.rewrite(build()))
