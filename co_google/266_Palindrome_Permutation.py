#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/palindrome-permutation/description/

Given a string,
determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
"""


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import collections

        table = collections.Counter(s)
        cnt = 0

        for i in table:
            if table[i] % 2:
                cnt += 1
            if cnt > 1:
                return False

        return True


def build():
    return "cd"
    return "code"
    return "carerac"
    return "aab"


if __name__ == "__main__":
    s = Solution()
    result = s.canPermutePalindrome(build())
    print(result)
