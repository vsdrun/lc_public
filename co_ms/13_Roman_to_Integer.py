#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/roman-to-integer/description/

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Symbol	I	V	X	L	C	D	M
Value	1	5	10	50	100	500	1,000

https://en.wikipedia.org/wiki/Roman_numerals
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000, 'D': 500, 'C': 100,
                 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        z = 0

        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]

        return z + roman[s[-1]]

    def rewrite(self, s):
        """
        :type s: str
        :rtype: int
        """
        from __builtin__ import xrange

        roman = {'M': 1000, 'D': 500, 'C': 100,
                 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        summ = 0

        # why? because there could be single char.
        for i in xrange(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                summ -= roman[s[i]]
            else:
                summ += roman[s[i]]

        summ += roman[s[-1]]

        return summ


def build():
    return "MCMLCVI"  # 1956
    return "DCXXI"  # 621
    return "MMM"  # 3000
    return "X"


if __name__ == "__main__":

    s = Solution()
    print(s.romanToInt(build()))
    print(s.rewrite(build()))
