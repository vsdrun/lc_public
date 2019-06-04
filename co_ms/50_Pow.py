#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/powx-n/description/

Implement pow(x, n).
"""


class Solution(object):

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)  # -n

        if n % 2:  # % 2, 得0 or 1
            return x * self.myPow(x, n - 1)

        return self.myPow(x * x, n / 2)


if __name__ == "__main__":
    s = Solution()
    r = s.myPow(2, 3)  # 2^3
    print(r)
