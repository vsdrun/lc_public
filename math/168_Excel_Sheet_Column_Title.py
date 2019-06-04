#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/excel-sheet-column-title/description/

Given a positive integer,
return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str

        corner case:  26/52/...
        """

        result = []

        anum = ord('A')

        q, r = divmod(n - 1, 26)

        result.append(r + anum)

        while q:
            q, r = divmod(q - 1, 26)
            result.append(r + anum)

        return "".join(map(chr, result[::-1]))


def build():
    return 750
    return 26
    return 52
    return 28
    return 23
    return 27


if __name__ == "__main__":

    s = Solution()
    result = s.convertToTitle(build())
    print(result)
