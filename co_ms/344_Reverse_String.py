#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/reverse-string/description/

Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)

        for idx in range(len(s) / 2):
            s[idx], s[~idx] = s[~idx], s[idx]

        return "".join(s)

def build():
    return "A man, a plan, a canal: Panama"


if __name__ == "__main__":
    s = Solution()
    print(s.reverseString(build()))
