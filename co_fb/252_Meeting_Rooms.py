#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/meeting-rooms/description/

Given an array of meeting time intervals consisting of
start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
"""


# Definition for an interval.

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def canAttendMeetings(self, intervals):
        """
        !!Better.
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x.start)

        # 現在比上之前.
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True


def build():
    return [
        Interval(0, 15),
        Interval(16, 20),
        Interval(13, 20),
        Interval(21, 22)
    ]

    return [Interval(0, 30),
            Interval(5, 10),
            Interval(15, 20)]


if __name__ == "__main__":
    s = Solution()
    print(s.canAttendMeetings(build()))
