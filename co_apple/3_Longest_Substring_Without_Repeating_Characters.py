#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string, find the length of the longest substring without
repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.

Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.


這種題目明顯用 2 pointers

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections as cc

        htable = cc.defaultdict(list)
        left, right = 0, 0

        mx = float("-inf")

        while right < len(s):
            if s[right] in htable:
                #  left 只往右走 不會回頭 故:
                left = max(left, htable[s[right]][-1] + 1)

            htable[s[right]].append(right)

            mx = max(mx, right - left + 1)

            right += 1

        print(htable)

        return mx


def build():
    return "abba"
    return "pwwke"
    return "c"
    return "dvdf"
    return "cc"


if __name__ == "__main__":
    s = Solution()
    result = s.lengthOfLongestSubstring(build())
    print(result)
