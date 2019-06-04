#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/merge-intervals/description/

Given a collection of intervals, merge all overlapping intervals.

example:
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
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

    def rewrite(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []

        intervals.sort(key=lambda i: i.start)

        for i in intervals:
            if not result or i.start > result[-1].end:
                result.append(i)
                continue

            if i.start <= result[-1].end:
                result[-1].end = max(result[-1].end, i.end)

        return result


def build():
    input = [[1, 3], [2, 6], [8, 10], [15, 18]]
    input = [[1, 4], [1, 5]]
    input = [[1, 4], [0, 4]]
    input = [[1, 4], [4, 5]]
    input = [[1, 4], [5, 6]]
    result = []

    for l, r in input:
        result += Interval(l, r),

    return result


if __name__ == "__main__":
    s = Solution()
    result = s.merge(build())
    print(result)
    result = s.rewrite(build())
    print(result)
