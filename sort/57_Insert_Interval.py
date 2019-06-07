#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/insert-interval/

Given a set of non-overlapping intervals,
insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted
according to their start times.

Example 1:
Given intervals [1,3],[6,9],
insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16],
insert and merge [4,9] in as [1,2],[3,10],[12,16].
This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""


class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        left, right = [], []

        for i in intervals:
            if i.end < s:
                left += i,
            elif i.start > e:
                right += i,
            else:
                s = min(s, i.start)
                e = max(e, i.end)

        return left + [Interval(s, e)] + right

def build():
    input = [[1, 3], [6, 9]]
    result = []

    for l, r in input:
        result += Interval(l, r),

    return result

def pp(ll):
    result = []

    for l in ll:
        result.append([l.start, l.end])

    print(result)

if __name__ == "__main__":
    s = Solution()
    pp(s.insert(build(), Interval(2, 5)))
