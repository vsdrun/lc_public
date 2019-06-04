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
        print(set(s))

        for c in sorted(set(s)):
            print("c: {0}".format(c))
            print(s.index(c))

            suffix = s[s.index(c):]

            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))

        return ''


def build_input():
    result = "ecbacdcbc"
    result = "dab"
    return result


if __name__ == "__main__":
    input = build_input()

    s = Solution()
    result = s.removeDuplicateLetters(input)

    # eacdb
    print(result)
