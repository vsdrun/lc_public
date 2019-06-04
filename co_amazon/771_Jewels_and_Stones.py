#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/jewels-and-stones/description/

You're given strings J representing the types of stones that are jewels,
and S representing the stones you have.
Each character in S is a type of stone you have.
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct,
and all characters in J and S are letters.

Letters are case sensitive, so "a" is
considered a different type of stone from "A".

Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3


Example 2:
Input: J = "z", S = "ZZ"
Output: 0
"""


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        from collections import Counter as cc

        cj = cc(J)
        cs = cc(S)

        cnt = 0

        for k in cs.keys():
            if k in cj:
                cnt += cs[k]

        return cnt


def build():
    return 'aA', 'aAAbbbb'


if __name__ == "__main__":
    s = Solution()
    print(s.numJewelsInStones(*build()))
