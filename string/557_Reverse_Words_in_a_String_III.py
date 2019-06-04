#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

Given a string, you need to reverse the order of characters in each word
within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not
be any extra space in the string.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = s[::-1].split()
        return " ".join(ret[::-1])


def build():
    return "Let's take LeetCode contest"


if __name__ == "__main__":

    s = Solution()
    print(s.reverseWords(build()))
