#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/flatten-2d-vector/description/

Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]

By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,2,3,4,5,6].
"""


class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vv = vec2d[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.vv.pop()

    def hasNext(self):
        """
        :rtype: bool
        """

        while self.vv and isinstance(self.vv[-1], list):
            vtmp = self.vv.pop()

            if not vtmp:
                continue

            self.vv.extend(vtmp[::-1])

        if self.vv:
            return True
        else:
            return False


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())


def build():
    return [[], [3]]
    return [
        [1, 2],
        [3],
        [4, 5, 6]
    ]


if __name__ == "__main__":
    i, v = Vector2D(build()), []

    while i.hasNext():
        v.append(i.next())

    print(v)
