#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def wordBreak(self):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        """
        ["cat", "cats", "and", "sand", "dog"]
        catsanddog len=10
        """
        a = [0, 1, 2, 3]
        b = [7, 8, 9, 10]
        c = [(i, j) for i in a if i > 2 for j in b]
        print(c)


if __name__ == "__main__":
    s = Solution()
    result = s.wordBreak()

    print(result)
