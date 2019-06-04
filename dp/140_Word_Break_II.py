#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/word-break-ii/description/

Given a non-empty string s and a dictionary wordDict containing a list
of non-empty words, add spaces in s to construct a sentence where each
word is a valid dictionary word. You may assume the dictionary does not
contain duplicate words.

重點是要:
Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set
of strings). Please reload the code definition to get the latest changes.
"""


class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        """
        ["cat", "cats", "and", "sand", "dog"]
        catsanddog len=10
        """
        # DP, using matrix to save result
        # DFS recursive.
        # Double for loop comprehension. If the second for loop is empty,
        # whole double for loop comprehension is empty.

        # 最後一個字母開始能組成什麼字呢? 沒有!
        memo = {len(s): ['']}

        def sentences(i):
            # i as start index, won't change.
            # j as end moving index, changes.
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in range(i + 1, len(s) + 1)
                           if s[i:j] in wordDict
                           for tail in sentences(j)]
            return memo[i]

        return sentences(0)

    def rewrite(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        """
        ["cat", "cats", "and", "sand", "dog"]
        catsanddog len=10
        ij
        i j
        i  j...
         ij
         i j
         i  j...
        """
        result = {len(s): ['']}


        def parse(idx):
            if idx not in result:  # 重要! 不然會重複!
                for mv_idx in range(idx + 1, len(s) + 1):
                    if s[idx:mv_idx] in wordDict:

                        for r in parse(mv_idx):
                            if not result.get(idx):
                                result[idx] = []

                            result[idx].append(
                                    s[idx:mv_idx] + " " + r if r else
                                    s[idx:mv_idx])

            return result[idx]


        return parse(0)


def build_input():
    return ["cat", "cats", "and", "sand", "dog"]


if __name__ == "__main__":
    n = build_input()

    s = Solution()
    #  ["cats and dog", "cat sand dog"]
    print(s.wordBreak("catsanddog", n))
    print(s.rewrite("catsanddog", n))

