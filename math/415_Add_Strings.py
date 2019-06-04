#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/add-strings/

Given two non-negative integers num1 and num2 represented as string,
return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        use ord
        """
        num1 = list(num1)
        num2 = list(num2)

        def add(num1):
            c1 = 0
            for idx, n1 in enumerate(num1[::-1]):
                c1 = c1 + (ord(n1) - ord('0'))*(10**idx)
            return c1

        return str(add(num1) + add(num2))


    def rewrite(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1)+int(num2))



def build():
    return "123", "123"


if __name__ == "__main__":
    s = Solution()
    print(s.addStrings(*build()))
