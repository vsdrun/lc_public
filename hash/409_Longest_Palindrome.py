#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/longest-palindrome/description/

Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        sdict = {}

        for c in s:
            if c in sdict:
                sdict[c] += 1
            else:
                sdict[c] = 1

        length = 0

        # 以判斷 奇數偶數
        odd = False

        for _, v in sdict.iteritems():
            if not v % 2:
                length += v
            else:
                if v == 1 and not odd:
                    length += v
                    odd = True
                else:
                    oddadd = v - 1
                    length += oddadd

                    if not odd:
                        length += 1
                        odd = True

        return length


def build_input():
    return "bananas"  # 5
    return "AAAccccdd"


if __name__ == "__main__":
    s = build_input()
    r = Solution()
    result = r.longestPalindrome(s)
    print(result)
