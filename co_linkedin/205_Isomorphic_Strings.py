#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/isomorphic-strings/description/

Given two strings s and t, determine if they are isomorphic.

isomorphic: corresponding or similar in form and relations.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters.

No two characters may map to the same character but a
character may map to itself.


For example,
Given "egg", "add", return true.
Given "foo", "bar", return false.
Given "paper", "title", return true.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = {}, {}

        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]

        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]

        print(d1)
        print(d2)
        print(d1.values())
        print(d2.values())
        return sorted(d1.values()) == sorted(d2.values())

        # or
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


def build():
    return "egg", "add"
    return "paper", "title"
    return "ab", "aa"


if __name__ == "__main__":

    s = Solution()
    print(s.isIsomorphic(*build()))
