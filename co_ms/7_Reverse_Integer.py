#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/reverse-integer/description/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output:  321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        #  s = cmp(x, 0)
        #  r = int(`s*x`[::-1])
        #  return s * r * (r < 2**31)

        from __builtin__ import xrange

        sx = str(x)[1:] if x < 0 else str(x)
        lsx = list(sx)

        llen = len(lsx)

        for i in xrange(llen / 2):

            lsx[i], lsx[~i] = lsx[~i], lsx[i]

        result = "".join(lsx) if x > 0 else "-" + "".join(lsx)
        #  print(-2 ** 31)
        #  print(2 ** 31)
        #  print(int(result))
        return int(result) if - 2 ** 31 <= int(result) < 2**31 else 0

    def rewrite(self, x):
        """
        :type x: int
        :rtype: int
        use stack
        """

        result = []

        if x < 0:
            sign = True
            x = -x
        else:
            sign = False

        while x:
            result.append(x%10)
            x /= 10

        total = 0

        for i, n in enumerate(result[::-1]):
            total += (10**i * n)

        if total > 2**31:
            total = 0

        return -total if sign else total


def build():
    return 1534236469
    return -1234
    return -2147483648
    return 123
    return 1563847412


if __name__ == "__main__":

    s = Solution()
    print(s.reverse(build()))
    print(s.rewrite(build()))
