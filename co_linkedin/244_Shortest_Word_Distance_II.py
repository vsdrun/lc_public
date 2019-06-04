#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/shortest-word-distance-ii/description/


This is a follow up of Shortest Word Distance.
The only difference is now you are given the list of words and your
method will be called repeatedly many times with different parameters.
**
How would you optimize it?

Design a class which receives a list of words in the constructor,
and implements a method that takes two words word1 and word2 and return
the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2,
and word1 and word2 are both in the list.
"""


class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        from collections import defaultdict

        self.d = defaultdict(list)

        for i, w in enumerate(words):
            self.d[w] += i,  # guarranteed from small to large since its index.

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        w1idx = self.d[word1]
        w2idx = self.d[word2]

        # cross compare due to the fact far left no need to compare with far
        # right idx.

        i, j = 0, 0
        m, n = len(w1idx), len(w2idx)
        min_dist = float("inf")

        while i < m and j < n:
            if w1idx[i] < w2idx[j]:
                min_dist = min(min_dist, w2idx[j] - w1idx[i])
                i += 1
            else:
                min_dist = min(min_dist, w1idx[i] - w2idx[j])
                j += 1

        return min_dist


def build(cnt):
    if cnt == 1:
        return "practice", "perfect"
    if cnt == 2:
        return "makes", "coding"

# practice: 1
# perfect: 0, 3

if __name__ == "__main__":
    s = WordDistance(["perfect", "practice", "makes",
                      "perfect", "coding", "makes"])
    print(s.shortest(*build(1)))
    print(s.shortest(*build(2)))
