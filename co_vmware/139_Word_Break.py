#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/word-break/

Given a non-empty string s and a dictionary wordDict containing a list
of non-empty words, determine if s can be segmented into a
space-separated sequence of one or more dictionary words. You may assume
the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE(2017 / 1 / 4):
The wordDict parameter had been changed to a list of strings (instead of
a set of strings). Please reload the code definition to get the latest
changes.
"""


class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        """
        s = lcoa
        dict = ["lco", "lcoa", "coa"]

        代表input s的每個char位置(含以前)的string是否在word dict內.
        [True, False, False, True, True]

        一定要測試 ok[j] 因為這代表著ok[j]以前的字有沒有中，
        如果沒有，則即使s[j:i]中也不能算，因為之前的字為孤魂野鬼，沒中.
        """
        from __builtin__ import xrange

        ok = [True]

        # 由1為始
        for i in xrange(1, len(s) + 1):
            ok += any(
                # 重要，一定要測 ok[j], 代表j以前的字有match,
                # j 之後的match才有意義.
                ok[j] and s[j:i] in wordDict
                for j in xrange(i)),

        return ok[-1]

    def rewrite(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for rhs in range(1, len(dp)):
            for lhs in range(rhs):
                if dp[rhs]:
                    break
                if dp[lhs] and s[lhs:rhs] in wordDict:
                    dp[rhs] = True

        return dp[-1]


def build():
    # lcoa
    return "lcoa", ["lco", "lcoa", "coa"]
    return "lcoa", ["l", "c", "o"]
    return "lcoa", ["l", "c", "oa"]


if __name__ == "__main__":
    s = Solution()

    print(s.wordBreak(*build()))
    print(s.rewrite(*build()))
