#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools


"""
https://leetcode.com/problems/letter-case-permutation/description/

Given a string S,
we can transform every letter individually to be lowercase or uppercase to
create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
"""


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]

        # https://docs.python.org/2/library/itertools.html#itertools.product
        # Roughly equivalent to nested for-loops in a generator expression.
        # For example, product(A, B) returns the same as
        # ((x,y) for x in A for y in B).
        return [''.join(i) for i in itertools.product(*L)]


def build():
    return "a1b2"


if __name__ == "__main__":
    s = Solution()
    result = s.letterCasePermutation(build())
    print(result)
