#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/wildcard-matching/description/

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).


The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""


class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        1. by concrete example.
        2. "*" is eager match, need to backtrack
        """
        tmp_p = None
        tmp_s = None

        while s:
            # 1:1 match test
            if p and (p[0] == "?" or p[0] == s[0]):
                p, s = p[1:], s[1:]
                continue

            # if p has *, preserve current p and s
            # p += 1
            # make a snapshot here.
            # p moves on.
            # This act as back trace.
            #  "abefcdgiescdfimde", "ab*cd?i*de"
            if p and p[0] == "*":
                tmp_p = p[:]
                tmp_s = s[:]
                p = p[1:]
                continue

            #  "abef cdgi escdfim de", "ab* cd?i*de"
            if tmp_p:
                p = tmp_p[1:]
                tmp_s = tmp_s[1:]  # 吃掉一個s吧 給* :-)
                s = tmp_s
                continue

            return False

        while p and p[0] == "*":
            p = p[1:]

        return False if p else True

    def rewrite(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """


def build():
    return "abefcdgiescdfimde", "ab*cd?i*de"


if __name__ == "__main__":
    s = Solution()
    print(s.isMatch(*build()))
    print(s.rewrite(*build()))
