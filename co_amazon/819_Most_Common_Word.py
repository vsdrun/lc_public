#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/most-common-word/description/


Given a paragraph and a list of banned words, return the most frequent
word that is not in the list of banned words.
It is guaranteed there is at least one word that isn't banned,
and that the answer is unique.

Words in the list of banned words are given in lowercase,
and free of punctuation.

Words in the paragraph are not case sensitive.  The answer is in lowercase.


Example:
Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"

Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does),
so it is the most frequent non-banned word in the paragraph.


Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
"""


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        from collections import Counter as cc
        from __builtin__ import unicode
        import re

        bp = map(unicode.lower, banned)

        cp = re.sub(r'[^a-zA-Z]', ' ', paragraph).lower().split()

        cp_cnt = cc([w for w in cp if w not in bp])

        result = cp_cnt.most_common()[0][0]
        return result


def build():
    return u"Bob hit a ball, the hit BALL flew far after it was hit.", [u"hit"]


if __name__ == "__main__":
    s = Solution()
    print(s.mostCommonWord(*build()))
