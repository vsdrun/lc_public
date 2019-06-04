#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/count-numbers-with-unique-digits/description/

Given a non-negative integer n, count all numbers with unique digits,
x, where 0 ≤ x < 10^n.

Example:
Given n = 2, return 91.
(The answer should be the total numbers in the range of
0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
"""

"""
IDEA:
1. 至多只有10位數 (即 < 10^11)
有可能每個數字都不同，超過10位數則一定不可能所有數字為unique.

2. C(9,1) * C(9,1) * C(8,1) * ... * C(1,1)

排列:
    P(N,R) = N! / (N-R)!
組合:
    C(N,R) = N! / R!(N-R)!

重複組合
    (N - 1 + R)! / R!*(N-1)!
"""


class Solution(object):

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n 表示10 ^ n
        # n == 1 -> 10 , 即<10 , 即只有一位數
        # n == 2 -> 100 , 即 <100 , 即只有兩位數
        if n == 0:
            return 1

        result = [0] * n

        # 至多有 10 位數可有獨立數字
        count = 10

        # buttom up approach
        for i in xrange(1, n + 1):
            if i == 1:
                # 當只有一位數時，共有0~9個不同, 即10個不同.
                result[i - 1] = count
                count -= 1
                continue
            if i == 2:
                # 兩位數時，共有9 * 9 個不同 最左位數不含0, 故為9.
                result[i - 1] = count * count
                count -= 1
                continue
            if i > 10:
                # 超過10位數，則不可能有unique numbers.
                result[i - 1] = 0
                continue

            result[i - 1] = count * result[i - 1 - 1]
            count -= 1

        return sum(result)


def build_input():
    return 11


if __name__ == "__main__":
    n = build_input()

    s = Solution()
    result = s.countNumbersWithUniqueDigits(n)

    # 91
    print(result)
