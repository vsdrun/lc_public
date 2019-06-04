#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/partition-labels/description/


A string S of lowercase letters is given.

We want to partition this string into as many parts as possible

**so that each letter appears in at most one part,

and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbaca defegde hijhklij"
Output: [9,7,8]

Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.

a: 4
b: 3
c: 2

d: 2
e: 3
f: 1
g: 1

h: 2
i: 2
j: 2
k: 1
l: 1


A partition like "ababcbacadefegde", "hijhklij"
is incorrect, because it splits S into less parts.
"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]

        Input: S = "ababcbaca defegde hijhklij"
        """

        from collections import Counter as cc
        from __builtin__ import xrange

        current_set = set()
        cs = cc(S)
        result = []

        last_idx = 0

        for i in xrange(len(S)):
            current_set.add(S[i])
            cs[S[i]] -= 1

            if cs[S[i]] == 0:
                current_set.remove(S[i])

                if not current_set:
                    result.append(i - last_idx + 1)
                    last_idx = i + 1

        return result


def build():
    return "ababcbacadefegdehijhklij"


if __name__ == "__main__":

    s = Solution()
    print(s.partitionLabels(build()))
