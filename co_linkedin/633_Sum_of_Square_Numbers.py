#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/sum-of-square-numbers/description/

Given a non-negative integer c,
your task is to decide whether there're two integers
a and b such that a**2 + b**2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: 3
Output: False


0 is integer!!!
ref:
https://leetcode.com/problems/sum-of-square-numbers/discuss/104973/Python-Straightforward-with-Explanation
"""


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        這是白痴解法 請忽略...
        """
        import math as m
        from __builtin__ import xrange

        def recursive(num, cnt):
            if cnt > 1:
                return False

            pivot = int(m.sqrt(num))

            for n in xrange(pivot, -1, -1):
                next_num = num - n ** 2

                if not next_num and cnt < 2:
                    return True

                if recursive(next_num, cnt + 1):
                    if not cnt:
                        return True

            return False

        return recursive(c, 0)

    def judgeSquareSum_2(self, c):
        """
        :type c: int
        :rtype: bool
        正解. 我們只在乎兩個數...
        """
        from __builtin__ import xrange

        def is_square(N):
            # 測試剩餘的這個數是否為 sqrt-able.
            return int(N**.5)**2 == N

        return any(is_square(c - a * a)
                   for a in xrange(int(c**.5), -1, -1))

    def judgeSquareSum_3(self, c):
        """
        :type c: int
        :rtype: bool
        完美解.
        """
        import math

        # 夾擠!!!
        ll, rr = 0, int(math.sqrt(c))

        while ll <= rr:
            mid = ll * ll + rr * rr
            if mid < c:
                ll += 1
            elif mid > c:
                rr -= 1
            else:
                return True

        return False


def build():
    return 999999999
    return 4
    return 102  # endless recursive! why?
    return 10081
    return 999999999
    return 5
    return 2
    return 3


if __name__ == "__main__":
    s = Solution()
    print(s.judgeSquareSum_2(build()))
    print(s.judgeSquareSum_3(build()))
