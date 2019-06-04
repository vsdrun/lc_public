#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/first-unique-character-in-a-string/description/

Given a string,
find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter as C

        c = C(s)
        print(c)

        for i, v in enumerate(s):
            if c[v] == 1:
                return i

        return -1


def build():
    return "loveleetcode"


if __name__ == "__main__":
    r = Solution()
    result = r.firstUniqChar(build())
    print(result)
