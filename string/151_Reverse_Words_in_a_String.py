#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/reverse-words-in-a-string/description/

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])


def build():
    return "   a   b "
    return ''
    return ' '
    return "the  sky is blue "
    return ' the sky'


if __name__ == "__main__":

    s = Solution()
    result = s.reverseWords(build())
    print(result)
