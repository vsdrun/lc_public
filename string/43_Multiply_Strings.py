#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/multiply-strings/description/

Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2.

Note:
The length of both num1 and num2 is < 110.

Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.

You must not use any built-in BigInteger library or
convert the inputs to integer directly.

"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        BETTER...
        product length = num1 + num2
        """
        product = [0] * (len(num1) + len(num2))
        pos = len(product) - 1

        for n1 in reversed(num1):
            tempPos = pos

            for n2 in reversed(num2):
                product[tempPos] += int(n1) * int(n2)
                product[tempPos - 1] += product[tempPos] / 10
                product[tempPos] %= 10
                tempPos -= 1
            pos -= 1

        pt = 0
        # 把前面多餘的0去掉~

        while pt < len(product) - 1 and product[pt] == 0:
            pt += 1

        return ''.join(map(str, product[pt:]))

    def multiply_too_complicated(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        def add(lhs, rhs):
            count_lhs = lhs
            count_rhs = rhs
            mask = 1
            carry_in = 0
            lsum = 0

            while count_lhs or count_rhs:
                lmasked = lhs & mask
                rmasked = rhs & mask
                carry_out = (lmasked & rmasked) | (carry_in & lmasked) | \
                    (carry_in & rmasked)
                lsum += lmasked ^ rmasked ^ carry_in

                carry_in = carry_out << 1
                count_lhs >>= 1
                count_rhs >>= 1
                mask <<= 1

            lsum += carry_in
            return lsum

        x = int(num1)
        y = int(num2)

        summ = 0

        while x:
            if x & 1:
                summ = add(summ, y)
            x >>= 1
            y <<= 1

        return str(summ)


def build():
    return "0", "0"
    return "4", "5"


if __name__ == "__main__":
    s = Solution()
    result = s.multiply(*build())

    print(result)
