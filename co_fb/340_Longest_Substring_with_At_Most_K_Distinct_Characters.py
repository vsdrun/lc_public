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
        # Use dictionary d to keep track of (character, location) pair,
        # where location is the rightmost location that the character appears at
        d = {}
        low, ret = 0, 0

        for i, c in enumerate(s):
            d[c] = i

            if len(d) > k:
                low = min(d.values())
                del d[s[low]]
                low += 1

            ret = max(i - low + 1, ret)

        return ret


def build():
    return "eceba", 2
    return "a", 1
    return "abcdeffgghh", 2


if __name__ == "__main__":
    st, k = build()

    s = Solution()
    result = s.lengthOfLongestSubstringKDistinct(st, k)

    print(result)
