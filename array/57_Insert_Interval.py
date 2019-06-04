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

    def insert_slow(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # You may assume that the intervals were initially sorted according to
        # their start times.
        # 注意輸入只有一個的corner case.

        if not intervals:
            return [[newInterval.start, newInterval.end]]

        result = []
        current_l = newInterval.start
        current_r = newInterval.end
        added = False

        for i in intervals:
            if added:
                result += [i.start, i.end],
                continue

            if current_l > i.end:
                result += [i.start, i.end],
                continue

            if current_r < i.start:
                if not added:
                    result += [current_l, current_r],
                    added = True
                result += [i.start, i.end],
                continue

            if current_l >= i.start:
                current_l = min(i.start, current_l)
                current_r = max(i.end, current_r)
                continue

            if i.start > current_r:
                if not added:
                    result += [current_l, current_r],
                    added = True
                result += [i.start, i.end],
                continue

            if current_r >= i.start and current_r <= i.end:
                current_r = max(i.end, newInterval.end)
                result += [current_l, current_r],
                added = True
                continue

        if not added:
            result += [current_l, current_r],

        return result

    def rewrite(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        分段概念

        left + xx + right
        """

        left, right = [], []

        l, r = newInterval.start, newInterval.end

        for i in intervals:
            if l > i.end:
                left += i,
            elif r < i.start:
                right += i,
            else:
                l = min(l, i.start)
                r = max(r, i.end)

        return left + [Interval(l, r)] + right


def build_input():
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
    input = build_input()

    s = Solution()
    pp(s.insert(input, Interval(2, 5)))
    pp(s.rewrite(input, Interval(2, 5)))
