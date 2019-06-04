#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

There are a number of spherical balloons spread in two-dimensional space.

For each balloon, provided input is the start and end coordinates
of the horizontal diameter.

Since it's horizontal,
y-coordinates don't matter and hence the x-coordinates of start and end of the
diameter suffice.
Start is always smaller than end. There will be at most 10^4 balloons.

An arrow can be shot up exactly vertically from different points along
the x-axis.

A balloon with xstart and xend bursts by an arrow shot at x if
xstart ≤ x ≤ xend.

There is no limit to the number of arrows that can be shot.
An arrow once shot keeps travelling up infinitely.
The problem is to find the minimum number of arrows that must
be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6
(bursting the balloons [2,8] and [1,6]) and
another arrow at x = 11 (bursting the other two balloons).


類似
554. Brick Wall

或是
253. Meeting Rooms II
"""


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int

        類似 253.
        先做 end/start sort

        概念建立:
        最小的end 是跟 start走 即唯一個pair
        此pair的start為箭穿過的min point.
        """
        import bisect as bi

        if not points:
            return 0

        end_s = sorted([p[1] for p in points])
        start_s = sorted(points, key=lambda x: x[0])

        arrow = 0
        curr_min_end = end_s[0]

        for st in start_s:
            if st[0] <= curr_min_end:
                idx = bi.bisect_left(end_s, st[1])
                end_s.pop(idx)
            else:
                arrow += 1
                curr_min_end = end_s[0]
                idx = bi.bisect_left(end_s, st[1])
                end_s.pop(idx)

        return arrow + 1

    def fast(self, points):
        """
        :type points: List[List[int]]
        :rtype: int

        類似 253.
        先做 end/start sort

        概念建立:
        最小的end 是跟 start走 即唯一個pair
        此pair的start為箭穿過的min point.
        """
        points = sorted(points, key=lambda x: x[1])
        res, end = 0, -float('inf')

        for interval in points:
            if interval[0] > end:
                res += 1
                end = interval[1]

        return res

    def rewrite(self, points):
        """
        :type points: List[List[int]]
        :rtype: int

        類似 253.
        先做 end/start sort

        概念建立:
        最小的end 是跟 start走 即唯一個pair
        此pair的start為箭穿過的min point.

        只要以一個end 為 pivot.
        """

        end = sorted(points, key=lambda p: p[1])
        moving_end = float("-inf")
        cnt = 0

        for e in end:
            if e[0] > moving_end:  # 反為 <= 之意.
                moving_end = e[1]
                cnt += 1

        return cnt


def build():
    return \
        [[77171087, 133597895], [45117276, 135064454], [80695788, 90089372], [91705403, 110208054], [52392754, 127005153],
         [53999932, 118094992], [11549676, 55543044], [43947739, 128157751], [55636226, 105334812], [69348094, 125645633]]
    return \
        [[0, 9], [1, 8], [7, 8], [1, 6], [9, 16], [
            7, 13], [7, 10], [6, 11], [6, 9], [9, 13]]
    return [[10, 16], [2, 8], [1, 6], [7, 12]]
    return []
    return [[4, 12], [7, 8], [7, 9], [7, 9], [2, 8], [6, 7], [5, 14], [4, 13]]


if __name__ == "__main__":
    s = Solution()
    print(s.findMinArrowShots(build()))
    print(s.rewrite(build()))
