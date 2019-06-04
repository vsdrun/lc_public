#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/reverse-words-in-a-string-ii/description/

Given an input string,
reverse the string word by word.
A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces
and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

Related problem: Rotate Array
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        from __builtin__ import xrange

        for i in xrange(len(s) / 2):
            s[i], s[~i] = s[~i], s[i]

        i = j = 0

        while j < len(s) + 1:

            if j == len(s) or s[j] == ' ':
                jj = j - 1

                while i < jj:
                    s[i], s[jj] = s[jj], s[i]
                    i += 1
                    jj -= 1

                i = j + 1
            j += 1

    def rewrite(self, s):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        from __builtin__ import xrange

        for i in xrange(len(s) / 2):
            s[i], s[~i] = s[~i], s[i]

        i = prev_idx = 0
        s += [' ']

        while i < len(s):
            if s[i] == ' ':
                o_i = i

                while prev_idx < i:
                    s[prev_idx], s[i - 1] = s[i - 1], s[prev_idx]
                    prev_idx += 1
                    i -= 1

                i = o_i
                prev_idx = i + 1

            i += 1
        s.pop()


def build():
    return ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s",
            " ", "b", "l", "u", "e"]


if __name__ == "__main__":

    s = Solution()
    str = build()
    s.reverseWords(str)
    print(str)
    str = build()
    s.rewrite(str)
    print(str)
