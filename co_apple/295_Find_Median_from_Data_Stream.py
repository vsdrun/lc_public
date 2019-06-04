#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
"""

import heapq


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lower_q = []  # max heap
        self.higher_q = []  # min heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        l_len = len(self.lower_q)
        h_len = len(self.higher_q)

        if l_len < h_len:
            heapq.heappush(self.higher_q, num)
            heapq.heappush(self.lower_q, -heapq.heappop(self.higher_q))
        elif l_len >= h_len:  # l_len > h_len
            if len(self.higher_q) and num < self.higher_q[0]:
                heapq.heappush(self.lower_q, -num)
                heapq.heappush(self.higher_q, -heapq.heappop(self.lower_q))
            else:
                heapq.heappush(self.higher_q, num)

        l_len = len(self.lower_q)
        h_len = len(self.higher_q)

        if l_len == h_len:
            self.result = (-self.lower_q[0] + self.higher_q[0]) / 2.0
        else:
            self.result = self.higher_q[0]

    def findMedian(self):
        """
        :rtype: float
        """
        return self.result


def build_list():
    l = [6, 10, 2, 6, 5, 0, 6, 3, 1, 0, 0]
    #  l = [-1, -2, -3, -4, -5]
    return l


if __name__ == "__main__":
    input_list = build_list()
    print("input: {0}".format(input_list))

    s = MedianFinder()

    for i in input_list:
        s.addNum(i)
        result = s.findMedian()
        print(result)
