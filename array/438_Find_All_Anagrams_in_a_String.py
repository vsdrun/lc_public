#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

Given a string s and a non-empty string p,
find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both
strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".



Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

不能用set... 因為有重複.
嘗試用 Counter.
"""


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]

        looking for signature.
        """
        if not s:
            return []

        from collections import Counter as cc

        result = []

        p_len = len(p)

        pc = cc(p)
        tmp_cc = cc()

        for i in range(len(s)):
            #  (s[i: i + p_len])

            tmp_cc.update([s[i]])

            if i >= p_len - 1:
                if pc == tmp_cc:
                    result += (i - p_len + 1),

                tmp_cc.subtract([s[i - p_len + 1]])

        return result

    def rewrite(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]

        looking for signature.
        """
        from collections import Counter as CC

        pcc = CC(p)
        tmp_cc = CC()
        result = []


        for idx in range(len(s)):
            tmp_cc.update(s[idx])

            if idx >= len(p) - 1:
                if tmp_cc == pcc:
                    result.append(idx - (len(p) - 1))

                tmp_cc.subtract([s[idx - (len(p) - 1)]])
            # 長度不到持續累加

        return result

def build():
    return "abab", "ab"
    return "cbaebabacd", "abc"


if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams(*build()))
    print(s.rewrite(*build()))
