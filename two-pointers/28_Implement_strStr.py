#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/implement-strstr/description/

Implement strStr().

Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int

        return haystack.find(needle)
        """

        ncnt = len(needle)

        if not needle:
            return 0

        if len(haystack) < ncnt:
            return -1

        for i, c in enumerate(haystack):
            if c == needle[0]:
                if haystack[i:i + ncnt] == needle:
                    return i

        return -1

    def rewrite(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        nlen = len(needle)

        if len(haystack) < nlen:
            return -1

        for i, c in enumerate(haystack):
            if c == needle[0]:
                if haystack[i: i + nlen] == needle:
                    return i

        return -1

    def cheat(self, haystack, needle):
        if needle not in haystack:
            return -1

        return haystack.find(needle)


def build():
    return "hello", "ll"
    return "", ""
    return "a", ""


if __name__ == "__main__":
    s = Solution()
    print(s.strStr(*build()))
    print(s.rewrite(*build()))
