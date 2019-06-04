#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/sentence-similarity/description/


Given two sentences words1, words2 (each represented as an array of strings),
and a list of similar word pairs pairs, determine if two sentences are similar.

For example, "great acting skills" and "fine drama talent" are similar,
if the similar word pairs are
pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].


不具有傳遞性!
Note that the similarity relation is not transitive.
For example,
if "great" and "fine" are similar, and "fine" and "good" are similar,
"great" and "good" are not necessarily similar.

有對等性!
However, similarity is symmetric.
For example, "great" and "fine" being similar is the same as
"fine" and "great" being similar.


自身相等!
Also, a word is always similar with itself.
For example,
the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar,
even though there are no specified similar word pairs.


Finally, sentences can only be similar if they have the same number of words.
So a sentence like words1 = ["great"] can
never be similar to words2 = ["doubleplus","good"].
"""


class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        白痴...
        是 1:n 關係...
        """
        from __builtin__ import xrange
        from collections import defaultdict as dd

        if len(words1) != len(words2):
            return False

        dmap = dd(list)

        for k, v in pairs:
            dmap[k].append(v)
            dmap[v].append(k)

        for i in xrange(len(words1)):
            if words1[i] == words2[i]:
                continue

            if words1[i] not in dmap or \
                    words2[i] not in dmap:
                return False

            if words2[i] not in dmap[words1[i]]:
                return False

        return True


def build():

    return ["an", "extraordinary", "meal"], \
        ["one", "good", "dinner"], \
        [["great", "good"], ["extraordinary", "good"], ["well", "good"], ["wonderful", "good"], ["excellent", "good"], ["fine", "good"], ["nice", "good"], ["any", "one"], ["some", "one"], ["unique", "one"], ["the", "one"], ["an", "one"], ["single", "one"], ["a", "one"], ["truck", "car"], ["wagon", "car"], ["automobile", "car"], ["auto", "car"], ["vehicle", "car"], [
            "entertain", "have"], ["drink", "have"], ["eat", "have"], ["take", "have"], ["fruits", "meal"], ["brunch", "meal"], ["breakfast", "meal"], ["food", "meal"], ["dinner", "meal"], ["super", "meal"], ["lunch", "meal"], ["possess", "own"], ["keep", "own"], ["have", "own"], ["extremely", "very"], ["actually", "very"], ["really", "very"], ["super", "very"]]

    return ["great", "acting", "skills"], ["fine", "drama", "talent"], \
        [["great", "fine"], ["acting", "drama"], ["skills", "talent"]]


if __name__ == "__main__":
    s = Solution()
    print(s.areSentencesSimilar(*build()))
