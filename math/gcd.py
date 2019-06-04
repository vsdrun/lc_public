#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
GCD
"""


class Solution(object):
    def gcd(self, x, y):
        if y == 0:
            return x
        return self.gcd(y, x % y)


def build():
    return 11, 8


if __name__ == "__main__":

    s = Solution()
    result = s.gcd(*build())
    print(result)
