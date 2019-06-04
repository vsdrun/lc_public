#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/group-anagrams/description/

Given an array of strings, group anagrams together.

For example, given: ["boo", "bob"]
Return:
將 含相同字母的放在一起.
[
["boo"],
["bob"]
]
"""


class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}

        for s in strs:
            s_sorted = "".join(sorted(s))

            if s_sorted in d:
                d[s_sorted].append(s)
            else:
                d[s_sorted] = [s]
        return d.values()

    def rewrite(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import Counter as cc
        result = dict()

        for w in strs:
            c = tuple(sorted(cc(w).items()))
            if c not in result:
                result[c] = list()

            result[c].append(w)

        return result.values()

    def rewrite2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dmap = dict()

        for s in strs:
            tmp = "".join(sorted(s))
            if dmap.get(tmp):
                dmap[tmp].append(s)
            else:
                dmap[tmp] = [s]

        return dmap.values()


def build():
    return ["cab", "pug", "pei", "nay", "ron", "rae", "ems", "ida", "mes"]
    return ["eat", "tea", "tan", "ate", "nat", "bat"]
    return ["boo", "bob"]


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(build()))
    print(s.rewrite(build()))
    print(s.rewrite2(build()))
    print(s.rewrite3(build()))
