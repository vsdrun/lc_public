#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/valid-palindrome-ii/description/

Given a non-empty string s,
you may delete at most one character.
Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True

Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z.
The maximum length of the string is 50000.
"""


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0

        # 由外向內夾擠...
        while i < len(s) / 2 and s[i] == s[-(i + 1)]:
            i += 1

        s = s[i:len(s) - i]

        # 跳過左邊 or 跳過右邊 將成就一個palindrome.
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]


def build():
    return "eeeed"
    return "aacdaa"
    return "abdca"
    return "ddcacd"


if __name__ == "__main__":
    s = Solution()
    print(s.validPalindrome(build()))
