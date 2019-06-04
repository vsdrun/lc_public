#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/valid-anagram/description/
Given two strings s and t ,
write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters?
How would you adapt your solution to such case?
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter as ct

        sct = ct(s)
        tct = ct(t)
        return sct == tct


def build():
    return "rat", "car"
    return "anagram", "nagaram"


if __name__ == "__main__":
    s = Solution()
    result = s.isAnagram(*build())
    print(result)
