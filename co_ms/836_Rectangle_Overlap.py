#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/rectangle-overlap/description/

A rectangle is represented as a list [x1, y1, x2, y2],
where (x1, y1) are the coordinates of its bottom-left corner,
and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.
To be clear,
two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Notes:

Both rectangles rec1 and rec2 are lists of 4 integers.
All coordinates in rectangles will be between -10^9 and 10^9.
"""

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool

        反向思考 怎樣不是overlap?
        剩下的就是overlap啦!
        """
        if rec1[0] >= rec2[2]: return False
        if rec1[2] <= rec2[0]: return False
        if rec1[1] >= rec2[3]: return False
        if rec1[3] <= rec2[1]: return False
        return True

def build():
    return [7,8,13,15], [10,8,12,20]
    return [0,0,1,1], [1,0,2,1]
    return [0,0,2,2], [1,1,3,3]


if __name__ == "__main__":
    s = Solution()
    print(s.isRectangleOverlap(*build()))
