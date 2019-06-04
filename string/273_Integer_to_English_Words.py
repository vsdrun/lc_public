#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/integer-to-english-words/description/


Convert a non-negative integer to its english words representation.
Given input is guaranteed to be less than 2^31 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
            Seven"
"""


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven ' \
            'Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen ' \
            'Nineteen'.split()

        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def words(n):
            if n < 20:  # 19
                return to19[n - 1:n]

            if n < 100:  # 92
                return [tens[n / 10 - 2]] + words(n % 10)

            if n < 1000:  # 978
                return [to19[n / 100 - 1]] + ['Hundred'] + words(n % 100)

            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):

                if n < 1000**(p + 1):  # 1000**2 , 1000**3, 1000**4
                    return words(n / 1000**p) + [w] + words(n % (1000**p))

        return ' '.join(words(num)) or 'Zero'


class Solution_2(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        v1 = "Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven " \
            " Twelve Thirteen Fourteen Fifteen Sixteen Seventeen " \
            "Eighteen Nineteen".split()
        v2 = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        v3 = "Thousand Million Billion".split()

        index = -1
        res = ""
        while num:
            temp = ""
            token = num % 1000
            num = num // 1000
            if token > 99:
                temp += v1[token // 100] + " Hundred "
                token = token % 100
            if token > 19:
                temp += v2[token // 10 - 2] + " "
                token = token % 10
            if token > 0:
                temp += v1[token]
            temp = temp.strip()
            if index >= 0 and temp:  # 貌似必须这么写。。真是无语啊
                temp = temp + " " + v3[index]
            res = temp + " " + res.strip()
            index += 1

        return res.strip() if res else v1[0]


def build():
    return 12302


if __name__ == "__main__":
    s = Solution_2()
    result = s.numberToWords(build())

    print(result)
