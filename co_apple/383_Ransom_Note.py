#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/ransom-note/description/

Given an arbitrary ransom note string and another string containing letters
from all the magazines,

write a function that will return true if the ransom note
can be constructed from the magazines ; otherwise, it will return false.

**
magazine裡的字只能被用一次!
Each letter in the magazine string can only be used once in your ransom note.


Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        O(m+n)
        https://docs.python.org/2/library/collections.html#collections.Counter
        """
        import collections

        result = collections.Counter(ransomNote) - collections.Counter(magazine)
        print(result)
        return not result


def build():
    return "aaa", "aab"
    return "aa", "aab"


if __name__ == "__main__":

    s = Solution()
    result = s.canConstruct(*build())
    print(result)
