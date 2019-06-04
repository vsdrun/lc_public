#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/rearrange-string-k-distance-apart/description/

Given a non-empty string s and an integer k,
rearrange the string such that the same characters are at
least distance k from each other.

All input strings are given in lowercase letters.
If it is not possible to rearrange the string, return an empty string "".

Example 1:
s = "aabbcc", k = 3
Result: "abcabc"
The same letters are at least distance 3 from each other.


Example 2:
s = "aaabc", k = 3
Answer: ""
It is not possible to rearrange the string.


Example 3:
s = "aaadbbcc", k = 2
Answer: "abacabcd"
Another possible answer is: "abcabcda"

The same letters are at least distance 2 from each other.
"""


class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        import collections as cc
        s = list(s)
        s.sort()
        result = cc.Counter(s)
        print(dir(result))
        print(result.most_common())


def build():
    return "aaadbbcc", 2
    return "aaabc", 3
    return "aabbcc", 3


if __name__ == "__main__":
    s = Solution()
    result = s.rearrangeString(*build())

    print(result)
