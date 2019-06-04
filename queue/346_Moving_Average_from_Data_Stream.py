#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/moving-average-from-data-stream/description/

Given a stream of integers and a window size,
calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""


class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.data = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """

        self.data += val,

        if len(self.data) > self.size:
            self.data = self.data[1:]
            return float(sum(self.data)) / self.size

        return float(sum(self.data)) / len(self.data)


if __name__ == "__main__":

    obj = MovingAverage(3)
    result = obj.next(1)
    result = obj.next(10)
    result = obj.next(3)
    result = obj.next(5)

    print(result)
