#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/meeting-rooms-ii/description/

Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""

# Definition for an interval.


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        e = ret = 0

        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)

        for s in range(len(start)):
            if start[s] < end[e]:
                ret += 1
            else:
                e += 1

        return ret

    def rewrite(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)

        ret = e = 0

        for s in start:
            if s < end[e]:
                ret += 1
            else:
                e += 1

        return ret

def build():
    return [Interval(0, 30), Interval(5, 10), Interval(15, 20)]


if __name__ == "__main__":

    s = Solution()
    print(s.minMeetingRooms(build()))
    print(s.rewrite(build()))
