#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/fraction-to-recurring-decimal/description/

Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""


class Solution(object):

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # 判斷 +-
        sign = '-' if numerator * denominator < 0 else ''

        q, r = divmod(abs(numerator), abs(denominator))
        result = [sign, str(q)]

        if r:
            result.append(".")

        remainder = []  # 看是否重複.

        while r:
            remainder.append(r)
            q, r = divmod(r * 10, abs(denominator))
            result.append(str(q))

            if r in remainder:
                back_index = len(remainder) - remainder.index(r)
                result = result[:-back_index] + \
                    ["("] + result[-back_index:] + [")"]
                break

        return "".join(result)


def build_input():
    #  return (1, 99)
    #  return (-2, 3)
    #  return (0, 2)
    #  return (2, 1)
    #  return (1, 2)
    return (2, 3)


if __name__ == "__main__":
    n, d = build_input()

    s = Solution()
    result = s.fractionToDecimal(n, d)

    print(result)
