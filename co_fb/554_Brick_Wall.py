#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/brick-wall/description/

There is a brick wall in front of you.
The wall is rectangular and has several rows of bricks.
The bricks have the same height but different width.
You want to draw a vertical line from the top to the
bottom and cross the least bricks.

The brick wall is represented by a list of rows.
Each row is a list of integers representing the width of each brick
in this row from left to right.

If your line go through the edge of a brick,
then the brick is not considered as crossed.
You need to find out how to draw the line to cross the least
bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall,
in which case the line will obviously cross no bricks.

Example:
Input:
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
Output: 2


The width sum of bricks in different rows are the same and won't exceed INT_MAX.
The number of bricks in each row is in range [1,10,000]. The height of wall is
in range [1,10,000]. Total number of bricks of the wall won't exceed 20,000.
"""


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        from __builtin__ import xrange
        import bisect as bi
        import collections as cc

        """

        >>> a=[1,2,3,444,444]
        >>> cc.Counter(a)
        Counter({444: 2, 1: 1, 2: 1, 3: 1})
        >>> cc.Counter(a).most_common(1)
        [(444, 2)]
        >>> cc.Counter(a).most_common()
        [(444, 2), (1, 1), (2, 1), (3, 1)]
        >>>
        """

        result = []
        # 用 hashtable 更好.

        for row in wall:
            sub_total = 0

            for i in xrange(len(row)):
                if len(row) > 1 and i != len(row) - 1:
                    sub_total += row[i]
                    bi.insort(result, sub_total)

        result = cc.Counter(result)
        print("result: {}".format(result))

        # 用binsort存 這樣 cc.Counter會快很多...
        result = cc.Counter(result).most_common(1)  # list of tuple(Key, Value)

        if result:
            return len(wall) - result[0][1]
        else:
            return len(wall)


def build():
    return [[1, 2, 2, 1],
            [3, 1, 2],
            [1, 3, 2],
            [2, 4],
            [3, 1, 2],
            [1, 3, 1, 1]]
    return [[1], [1], [1]]


if __name__ == "__main__":

    s = Solution()
    print(s.leastBricks(build()))
