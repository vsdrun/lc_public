#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/remove-duplicate-letters/description/

Given a string which contains only lowercase letters, remove duplicate
letters so that every letter appear once and only once. You must make
sure your result is the smallest in lexicographical order among all
possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""


class Solution(object):

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        for c in sorted(set(s)):

            suffix = s[s.index(c):]

            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))

        return ''

    def rewrite(self, s):
        """
        :type s: str
        :rtype: str
        Given "bcabc"
        Return "abc"
        這是一個recursive function, 也就是，
        一個run要解決什麼問題?
        1. 將字母第一個出現的保留，之後的設為'',
            之前的拋棄(如果之後的set==所有char set)
        2. 將剩下的字串丟入下一個recursive.
        """
        # 思考: 先將string裡的char build成set.
        sset = set(s)

        # sort it, because we need lexi order

        for c in sorted(sset):
            if sset == set(s[s.index(c):]):
                # we can get rid of previous chars since what's behind is
                # enough
                return c + self.rewrite(s[s.index(c):].replace(c, ''))

        return ''


def build():
    result = "ecbacdcbc"
    result = "dab"
    return result


if __name__ == "__main__":
    s = Solution()
    result = s.removeDuplicateLetters(build())
    print(result)
    result = s.rewrite(build())
    print(result)
