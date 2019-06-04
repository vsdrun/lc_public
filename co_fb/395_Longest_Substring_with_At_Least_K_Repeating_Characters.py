#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

Find the length of the longest substring T of a given string
(consists of lowercase letters only) such that every character in
T appears no less than k times.

Example 1:
Input:
s = "aaabb", k = 3
Output:
3
The longest substring is "aaa", as 'a' is repeated 3 times.


Example 2:
Input:
s = "ababbc", k = 2
Output:
5
The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
accccbb k = 2
"""


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))

        return len(s)

    def rewrite(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        abbbcdddeff , k = 2
        """

        def recount(s):
            cset = set(s)

            for c in cset:
                if s.count(c) < k:
                    return max([recount(sub) for sub in s.split(c)])

            return len(s)

        return recount(s)


def build():
    return "ababbc", 2  # ababb
    return "abbbcdddeff", 2


if __name__ == "__main__":
    s = Solution()
    print(s.longestSubstring(*build()))
    print(s.rewrite(*build()))
