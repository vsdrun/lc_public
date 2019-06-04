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

class MovingAverageRewrite(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.data = [] # [sum, previous sum]

    def next(self, val):
        """
        :type val: int
        :rtype: float
        Idea I used here is to cache the previous total and move forward
        However, the
        """
        if self.data:
            self.data.append([val + self.data[-1][0], self.data[-1][0]])
        else:
            self.data.append([val, 0])

        while len(self.data) > self.size:
            self.data[-1][0] = self.data[-1][0] - self.data[0][0] + \
                self.data[0][1]
            self.data = self.data[1:]

        result = float(self.data[-1][0]) / len(self.data)
        print("val: {} result: {} back: {}".format(val, result, self.data[-1]))

        print("list: {}".format(self.data))
        return result


if __name__ == "__main__":
    obj = MovingAverage(20)
    result = obj.next(-1)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-1)
    result = obj.next(-1)
    result = obj.next(-1)
    result = obj.next(-1)
    result = obj.next(-1)
    result = obj.next(-1)
    result = obj.next(-1)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    print(result)

    print("---------------")

    obj = MovingAverageRewrite(20)
    result = obj.next(-1)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-1)
    result = obj.next(-1)
    result = obj.next(-1)
    result = obj.next(-1)
    result = obj.next(-1)
    result = obj.next(-1)
    result = obj.next(-1)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    result = obj.next(-55)
    print(result)
