#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons)
is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        from __builtin__ import reduce

        if '' == digits:
            return []

        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        return reduce(lambda acc, digit: [x + y for x in acc for y in
                                          kvmaps[digit]], digits, [''])

    def rewrite(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        from __builtin__ import reduce

        if '' == digits:
            return []

        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # reduce 的[''] 為initial, 就是 acc.
        # digit 為digits的sequence elements.
        # first 為 ['']
        # second 為 digits[0]
        return reduce(
            lambda first, second:
                [f + s for f in first for s in kvmaps[second]], digits, [''])

    def rewrite2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        from __builtin__ import reduce

        if '' == digits:
            return []

        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def f(first, second):
            # first as [chars]
            # second as [digits]
            print("first: {}".format(first))
            print("second: {}".format(second))
            result = []

            for f in first:
                for s in kvmaps[second]:
                    result.append(f + s)

            print("result: {}".format(result))

            return result

        r = reduce(f, digits, [''])  # second, first
        print(r)
        return r

def build():
    return "23"


if __name__ == "__main__":
    s = Solution()
    #  print(s.letterCombinations(build()))
    #  print(s.rewrite(build()))
    print(s.rewrite2(build()))
