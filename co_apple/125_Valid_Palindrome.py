#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/valid-palindrome/description/

Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        si = 0
        ei = len(s) - 1

        while si < ei:
            while si < ei and not s[si].isalpha() and not s[si].isalnum():
                si += 1
            while si < ei and not s[ei].isalpha() and not s[ei].isalnum():
                ei -= 1

            if s[si].lower() != s[ei].lower():
                return False
            si += 1
            ei -= 1

        return True


def build():
    return "A man, a plan, a canal: Panama"


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(build()))
