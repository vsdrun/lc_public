#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/max-points-on-a-line/description/

Given n points on a 2D plane,
find the maximum number of points that lie on the same straight line.

https://leetcode.com/problems/max-points-on-a-line/discuss/47113/A-java-solution-with-notes

1. 算分子分母 GCD 並除以之.
2. 以str的方式存斜率 不要用 float...
"""


# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """


def build():
    return "MCMXCVI"  # 1996
    return "DCXXI"  # 621


if __name__ == "__main__":

    s = Solution()
    result = s.maxPoints(build())
    print(result)
