#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/integer-to-roman/description/

Roman numerals are represented by seven different symbols:
I, V, X, L, C, D and M.


Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral,
just two one's added together.
Twelve is written as, XII, which is simply X + II.
The number twenty seven is written as XXVII, which is XX + V + II.

*
Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is
written as IV.


Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.


Example 1:
Input: 3
Output: "III"

Example 2:
Input: 4
Output: "IV"

Example 3:
Input: 9
Output: "IX"

Example 4:
Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.

Example 5:
Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        max: 3999
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
        """

        # 4, 9 注意.
        # 其餘為base.
        result = []

        def check49(num):
            if num in (4, 9):
                return True
            return False

        while num:
            tmp = num
            base = None
            multiple = 0

        #  roman = {1000: 'M', 500: 'D', 100: 'C',
            #  50: 'L', 10: 'X', 5: 'V', 1: 'I'}
            #  MMMCMXCIX
            if num >= 1000:
                base = 'M'
                multiple = num/1000
                tmp -= 1000 * multiple
            elif 1000 > num >= 500:
                if check49(num / 100):
                    base = 'CM'
                    multiple = 1
                    tmp -= 900
                else:
                    base = 'D'
                    multiple = num/500
                    tmp -= 500 * multiple
            elif 500 > num >= 100:
                if check49(num / 100):
                    base = 'CD'
                    multiple = 1
                    tmp -= 400
                else:
                    base = 'C'
                    multiple = num/100
                    tmp -= 100 * multiple
            elif 100 > num >= 50:
                if check49(num / 10):
                    base = 'XC'
                    multiple = 1
                    tmp -= 90
                else:
                    base = 'L'
                    multiple = num/50
                    tmp -= 50 * multiple
            elif 50 > num >= 10:
                if check49(num / 10):
                    base = 'XL'
                    multiple = 1
                    tmp -= 40
                else:
                    base = 'X'
                    multiple = num/10
                    tmp -= 10 * multiple
            elif 10 > num >= 5:
                if check49(num):
                    base = 'IX'
                    multiple = 1
                    tmp -= 9
                else:
                    base = 'V'
                    multiple = num/5
                    tmp -= 5 * multiple
            elif 5 > num >= 1:
                if check49(num):
                    base = 'IV'
                    multiple = 1
                    tmp -= 4
                else:
                    base = 'I'
                    multiple = num
                    tmp -= 1 * multiple

            result.append(base * multiple)
            num = tmp

        return "".join(result)

    def rewrite(self, num):
        """
        :type num: int
        :rtype: str
        最佳解!
        """

        """
        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        """
        dmap = {1:'I', #
                4:'IV',
                5:'V',#
                9:'IX',
                10:'X',#
                40:'XL',
                50:'L',#
                90:'XC',
                100:'C',#
                400:'CD',
                500:'D',#
                900:'CM',
                1000:'M'}#

        pivot = sorted(dmap.keys(), reverse=True)

        """
        Roman numerals are usually written largest to smallest from left to right.
        However, the numeral for four is not IIII. Instead, the number four is
        written as IV.
        """
        result = ""

        for p in pivot:
            if num >= p:
                quotient = num / p
                num %= p
                result += dmap[p] * quotient

        return result


def build():
    return 58
    return 9
    return 3999
    return 1994
    return 4
    return 3


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(build()))
    print(s.rewrite(build()))
