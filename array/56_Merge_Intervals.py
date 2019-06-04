#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/merge-intervals/description/

Given a collection of intervals, merge all overlapping intervals.

example:
Given   [1,3],[2,6],[8,10],[15,18],
return  [1,6],[8,10],[15,18],
"""


class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        out = []
        s = sorted(intervals, key=lambda i: i.start)

        for i in s:
            if out and i.start <= out[-1][1]:
                out[-1][1] = max(out[-1][1], i.end)
            else:
                out += [i.start, i.end],

        return out


def build_input():
    input = [[1, 3], [2, 6], [8, 10], [15, 18]]
    input = [[1, 4], [1, 5]]
    input = [[1, 4], [0, 4]]
    result = []

    for l, r in input:
        result += Interval(l, r),

    return result


if __name__ == "__main__":
    input = build_input()

    s = Solution()
    result = s.merge(input)

    # [[1,6],[8,10],[15,18]]
    # [[0,4]]
    print(result)
