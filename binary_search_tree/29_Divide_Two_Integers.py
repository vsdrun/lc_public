#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/divide-two-integers/

Given two integers dividend and divisor,
divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.

Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−2^31,  2^31 − 1].

For the purpose of this problem, assume that your function returns 2^31 − 1
when the division result overflows.
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # smart...
        sign = (dividend < 0) is (divisor < 0)

        dividend, divisor = abs(dividend), abs(divisor)

        result = 0
        # 10 / 2 為例
        while dividend >= divisor:
            temp, quotient = divisor, 1

            while dividend > (temp<<1):
                temp <<= 1
                quotient <<= 1

            dividend -= temp
            result += quotient

        if sign:
            if result <= 2**31-1:
                return result
            else:
                return 2**31-1
        else:
            if result >= -(2**31):
                result = -result
                return result
            else:
                return -(2**31)


def build():
    return -7, -3
    return 7, -3
    return 0, -3
    return 1, 1


if __name__ == "__main__":
    s = Solution()
    print(s.divide(*build()))
