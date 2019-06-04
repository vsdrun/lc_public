#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/shortest-word-distance-iii/description/

This is a follow up of Shortest Word Distance.
The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2,
return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words
in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.
"""


class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        c_w = None
        c_i = -1
        dist = float("inf")
        same = False

        if word1 == word2:
            same = True

        for i, w in enumerate(words):
            if w != word1 and w != word2:
                continue

            if same and c_w:
                dist = min(dist, i - c_i)
            elif c_w and c_w != w:
                dist = min(dist, i - c_i)

            c_w = w
            c_i = i

        return dist


def build():
    return ["makes", "practice", "makes", "perfect", "coding", "makes"], \
        "makes", "perfect"
    return ["makes", "practice", "makes", "perfect", "coding", "makes"], \
        "makes", "makes"


if __name__ == "__main__":
    s = Solution()
    print(s.shortestWordDistance(*build()))
