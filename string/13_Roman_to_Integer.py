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


def build():
    return "MCMXCVI"  # 1996
    return "DCXXI"  # 621


if __name__ == "__main__":

    s = Solution()
    result = s.romanToInt(build())
    print(result)
