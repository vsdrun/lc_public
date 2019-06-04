#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/zigzag-iterator/description/

Given two 1d vectors,
implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]

By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors?
How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases.
If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic".


For example, given the following input:
[1,2,3]
[4,5,6,7]
[8,9]

It should return [1,4,8,2,5,9,3,6,7].
"""


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.flip = False

    def next(self):
        """
        :rtype: int
        """
        if not self.flip:
            ret, self.v1 = self.v1[:1], self.v1[1:]

            if not ret:
                ret, self.v2 = self.v2[:1], self.v2[1:]

        else:
            ret, self.v2 = self.v2[:1], self.v2[1:]

            if not ret:
                ret, self.v1 = self.v1[:1], self.v1[1:]

        self.flip = not self.flip

        return ret[0]

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.flip:
            if self.v1:
                return True
            elif self.v2:
                return True
        else:
            if self.v2:
                return True
            elif self.v1:
                return True
        return False


class ZigzagIteratorRewrite(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.dataIdx = 0
        self.data = [v1, v2]


    def next(self):
        """
        :rtype: int
        """
        ret, self.data[self.dataIdx] = \
                self.data[self.dataIdx][:1], self.data[self.dataIdx][1:]

        if self.dataIdx == len(self.data) - 1:
            self.dataIdx = 0
        else:
            self.dataIdx += 1

        return ret[0]

    def hasNext(self):
        """
        :rtype: bool
        """
        cycle = self.dataIdx
        init = True

        while init or cycle != self.dataIdx:
            init = False

            if self.data[self.dataIdx]:
                return True
            else:
                if self.dataIdx == len(self.data) - 1:
                    self.dataIdx = 0
                else:
                    self.dataIdx += 1

        return False



class ZigzagIteratorRewrite2(object):
    """
    Data! is the important thing in DoD.
    rearange data into a single list, smart...
    """
    def __init__(self, v1, v2):
        self.a=[]

        for i , j in zip(v1,v2):
            self.a.append(i)
            self.a.append(j)

        if len(v1)>len(v2):
            self.a.extend(v1[len(v2):])
        else:
            self.a.extend(v2[len(v1):])


    def next(self):
        return self.a.pop(0)


    def hasNext(self):
        return len(self.a)>0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())


def build():
    v1 = [1,2,3]
    v2 = [4,]
    return v1, v2

    v1 = []
    v2 = [1]
    return v1, v2


if __name__ == "__main__":

    z = ZigzagIterator(*build())

    while z.hasNext():
        print(z.next())
    print("----------")

    z = ZigzagIteratorRewrite(*build())

    while z.hasNext():
        print(z.next())
