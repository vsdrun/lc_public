#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/excel-sheet-column-number/description/


Given a column title as appear in an Excel sheet,
return its corresponding column number.


For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26

    AA -> 27
    AB -> 28
    ...


Example 1:
Input: "A"
Output: 1


Example 2:
Input: "AB"
Output: 28


Example 3:
Input: "ZY"
Output: 701
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        from __builtin__ import xrange

        s = list(s)
        hmap = dict()

        for i in xrange(26):
            hmap[chr(ord('A') + i)] = i + 1

        total = 0

        for i in xrange(len(s) - 1, -1, -1):
            print("i:{} ~i: {}".format(i, ~i))
            print(hmap)
            total += 26 ** i * hmap[s[~i]]

        return total


def build():
    return "ZY"


if __name__ == "__main__":

    s = Solution()
    print(s.titleToNumber(build()))
