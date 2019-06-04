#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/edit-distance/description/

Given two words word1 and word2,
find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')


Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        """
        subproblem:
        from left to right
        1. same char, move on
        2. different char
            Insert: Recur for m and n-1
            Remove: Recur for m-1 and n
            Replace: Recur for m-1 and n-1
        """


def build():
    return "horse", "ros"


if __name__ == "__main__":
    s = Solution()
    result = s.minDistance(*build())
    print(result)
