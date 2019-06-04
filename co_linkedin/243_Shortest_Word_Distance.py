#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/shortest-word-distance/description/


Given a list of words and two words word1 and word2,
return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

"""


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int

        注意邏輯! Very SMART!
        """

        ans = len(words)
        current_word, current_index = None, 0

        for index, word in enumerate(words):
            if word != word1 and word != word2:
                continue

            if current_word and word != current_word:
                ans = min(ans, index - current_index)

            current_word, current_index = word, index

        return ans


if __name__ == "__main__":
    s = Solution()
    r = s.shortestDistance(["perfect", "practice", "makes",
                            "perfect", "coding", "makes"],
                           "coding", "practice")
    print(r)
