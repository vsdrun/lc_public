#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/permutation-in-string/description/

Given two strings s1 and s2, write a function to return true if s2 contains
the permutation of s1.

In other words,
one of the first string's permutations is the substring of the second string.

1. 先算s1長度. if s2 < s1 , return

Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").


Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        from __builtin__ import xrange

        # 先算長度.
        s1_len, s2_len = len(s1), len(s2)

        if s1_len > s2_len:
            return False

        # 用數字比用char 好阿~
        # a1 , s1裡的signature
        a1 = [ord(c) - ord('a') for c in s1]
        # a2 , s2裡的signature
        a2 = [ord(c) - ord('a') for c in s2]


        target, window = [0] * 26, [0] * 26

        #  "ab" ,"eidbaooo"

        # target 中 有此字母的count + 1
        for c in a1:
            target[c] += 1

        # 依據s1長度來對s2相同idx處的char 做 + 1, 此為 漂移window
        for idx in xrange(s1_len):
            window[a2[idx]] += 1

        for idx in xrange(s1_len, s2_len):
            if window == target:
                return True

            window[a2[idx - s1_len]] -= 1
            window[a2[idx]] += 1

        if window == target:
            return True

        return False

    def rewrite(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        s1result , s2result = [0] * 26, [0] * 26

        s1ord = [ord(i) - ord('a') for i in s1]
        s2ord = [ord(i) - ord('a') for i in s2]

        # init. s1result
        for idx in range(len(s1)):
            s1result[s1ord[idx]] += 1

        # init. s2result with s1's length
        for idx in range(len(s1)):
            s2result[s2ord[idx]] += 1

        if s1result == s2result:
            return True

        for idx in range(len(s1), len(s2)):
            s2result[s2ord[idx - len(s1)]] -= 1
            s2result[s2ord[idx]] += 1

            if s1result == s2result:
                return True

        return False





def build():
    return "bc" ,"eidcbaooo"
    return "ab" ,"eidbaooo"


if __name__ == "__main__":
    s = Solution()
    print(s.checkInclusion(*build()))
    print(s.rewrite(*build()))
