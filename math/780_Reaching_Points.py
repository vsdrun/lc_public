#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/reaching-points/

A move consists of taking a point (x, y)
and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty),
return True if and only if a sequence of moves exists to transform the point
(sx, sy) to (tx, ty). Otherwise, return False.


Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

Note:

sx, sy, tx, ty will all be integers in the range [1, 10^9].

https://leetcode.com/problems/reaching-points/discuss/114856/JavaC%2B%2BPython-Modulo-from-the-End
"""

class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx

        return sx == tx and sy <= ty and (ty - sy) % sx == 0 or \
            sy == ty and sx <= tx and (tx - sx) % sy == 0

    def rewrite(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        A move consists of taking a point (x, y)
        and transforming it to either (x, x+y) or (x+y, y).

        Given a starting point (sx, sy) and a target point (tx, ty),
        return True if and only if
        a sequence of moves exists to transform the point
        (sx, sy) to (tx, ty).
        Otherwise, return False.
        x, y -> x+y, y -> x+y+y, y -> x+y+y+y, y
        """

        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx

        return sx == tx and sy <= ty and (ty - sy) % sx == 0 or \
                sy == ty and sx <= tx and (tx - sx) % sy == 0

def build():
    return 1, 1, 3, 5


if __name__ == "__main__":
    s = Solution()
    print(s.rewrite(*build()))
