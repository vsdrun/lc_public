#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/range-sum-query-2d-mutable/description/

https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/

https://brilliant.org/wiki/fenwick-tree/

https://www.youtube.com/watch?v=CWDQJGaN1gY
"""


class Fenwick():
    def update(self, i, x):  # add x to the ith position
        while i <= self.N:
            self.BIT[i - 1] += x  # because we're working with an 1-based array
            i += i & (-i)  # magic! don't touch!

    def query(self, i):  # find the ith prefix sum
        s = 0

        while i > 0:
            s += self.BIT[i - 1]
            i -= i & (-i)

        return s

    def __init__(self, ll=[]):  # initialize the fenwick tree

        self.N = len(ll)
        self.BIT = [0 for i in xrange(self.N)]

        for i in xrange(1, self.N + 1):
            self.update(i, ll[i - 1])


def build():
    return 1, 3


if __name__ == "__main__":
    s = Solution()
    result = s.licenseKeyFormatting(*build())

    print(result)
