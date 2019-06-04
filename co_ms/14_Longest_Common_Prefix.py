#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common
prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        """
        1. consider using reduce, really necessary?
        2. since it's prefix, that is to say, every char must exist in strings
        """
        # edge case
        if not strs:
            return ""

        max_index = 0

        # be ware, if any of the list is empty, zip won't work.
        for i, clist in enumerate(zip(*strs)):
            result = set(clist)

            if len(result) > 1:
                return strs[0][:i]
            # for edge case, like one of the str in list is ""
            max_index = i + 1
        else:
            return strs[0][:max_index]

    def rewrite(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        """
        1. consider using reduce, really necessary?
        2. since it's prefix, that is to say, every char must exist in strings
        """

        if not strs:
            return ''

        midx = 0

        # 如果有str為[], 則zip為[]
        for idx, val in enumerate(zip(*strs)):
            sset = set(val)

            if len(sset) > 1:
                # stops here...
                return strs[0][:midx]

            midx = idx + 1
        else:
            return strs[0][:midx]


def build_input():
    return ["aaa", "aaabc", "aaabbb", "aaabcdddd"]
    return ["abab", "aba", ""]


if __name__ == "__main__":
    n = build_input()
    s = Solution()
    print(s.longestCommonPrefix(n))
    print(s.rewrite(n))
