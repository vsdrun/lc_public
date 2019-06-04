#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/one-edit-distance/description/

Given two strings S and T, determine if they are both one edit distance apart.
"""


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str  小
        :type t: str  大
        :rtype: bool
        """
        if len(s) > len(t):
            # start with less length~
            return self.isOneEditDistance(t, s)

        if abs(len(s) - len(t)) > 1 or s == t:
            return False

        for i in range(len(s)):
            if s[i] != t[i]:
                # aba / aa
                return s[i + 1:] == t[i + 1:] or s[i:] == t[i + 1:]

        return True  # 都相同 只差一

    def rewrite(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        good logic...
        """
        lens, lent = len(s), len(t)

        if lens > lent:
            return self.isOneEditDistance(t, s)

        for i in xrange(lens):
            if s[i] != t[i]:
                step = 1 if lens == lent else 0
                return s[i + step:] == t[i + 1:]

        return lent - lens == 1


def build():
    return "ssss", "dsss"


if __name__ == "__main__":
    s = Solution()
    print(s.isOneEditDistance(*build()))
    print(s.rewrite(*build()))
