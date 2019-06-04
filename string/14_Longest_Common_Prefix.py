#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common "prefix"
string amongst an array of strings.
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


def build_input():
    return ["abab", "aba", ""]
#  return [""]
    #  return ["aaa","aaabc","aaabbb","aaabcdddd"]


if __name__ == "__main__":
    n = build_input()
    s = Solution()
    result = s.longestCommonPrefix(n)

    print(result)
