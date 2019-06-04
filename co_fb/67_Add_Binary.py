#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/add-binary/description/

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) == 0:
            return b

        if len(b) == 0:
            return a

        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'

        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1], b[0:-1]) + '0'
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + '1'

    def rewrite(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        if not len(a):
            return b

        if not len(b):
            return a

        if a[-1] == '1' and b[-1] == '1':
            return self.rewrite(self.rewrite(a[:-1], b[:-1]), '1') + '0'

        if a[-1] == '0' and b[-1] == '0':  # 注意 0, 0
            return self.rewrite(a[:-1], b[:-1]) + '0'
        else:
            return self.rewrite(a[:-1], b[:-1]) + '1'


def build():
    return "110010", "10111"
    return "101", "1"


if __name__ == "__main__":

    s = Solution()
    print(s.addBinary(*build()))
    print(s.rewrite(*build()))
