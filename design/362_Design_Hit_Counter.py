#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/design-hit-counter/

Design a hit counter which counts the number of hits received
in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and
you may assume that calls are being made to the system in chronological order
(ie, the timestamp is monotonically increasing).
You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:
HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301);
Follow up:
What if the number of hits per second could be very large?
Does your design scale?
"""
import bisect as bi

class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._5 = 60 * 5
        self.hits = [float("-inf")]


    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        bi.insort(self.hits, timestamp)


    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        right = timestamp # include
        left = right - self._5
        left = 0 if left < 0 else left  # exclude

        print("hits: {}".format(self.hits))
        print("right: {} left: {}".format(right, left))

        lidx = bi.bisect_right(self.hits, left)
        ridx = bi.bisect_right(self.hits, right)
        print("lidx: {} ridx: {}".format(lidx, ridx))

        return len(self.hits[lidx:ridx])

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

def build():
    pass

if __name__ == "__main__":
    #  ["HitCounter","hit","hit","hit","hit","getHits","hit","getHits"]
#  [[],[1],[1],[1],[300],[300],[300],[300]]

    s = HitCounter()
    s.hit(1)
    s.hit(2)
    s.hit(3)
    print(s.getHits(4)) # 3
    s.hit(300)
    print(s.getHits(300)) # 4
    print(s.getHits(301)) # 3

    print("------")
    s = HitCounter()
    s.hit(1)
    s.hit(1)
    s.hit(1)
    s.hit(300)
    print(s.getHits(300)) # 4
    s.hit(300)
    print(s.getHits(300)) # 5
