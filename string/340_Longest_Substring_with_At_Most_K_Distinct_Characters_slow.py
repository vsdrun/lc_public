#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/

Given a string, find the length of the longest substring T
that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
"""


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # think of sliding windows index

        i, j = 0, 1
        max_len = 0

        while j <= len(s):
            g_set = set()

            for c in s[i:j]:
                g_set.add(c)

            if len(g_set) <= k:
                max_len = max(max_len, j - i)
                j += 1
            else:
                i += 1

        return max_len


def build():
    return "a", 1
    return "abcdeffgghh", 2
    return "eceba", 2


if __name__ == "__main__":
    st, k = build()

    s = Solution()
    result = s.lengthOfLongestSubstringKDistinct(st, k)

    print(result)
