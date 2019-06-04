#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/container-with-most-water/description/

Given n non-negative integers a1, a2, ..., an ,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line
i is at (i, ai) and (i, 0).

Find two lines, which together with x-axis forms a container,
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        h = height

        if not len(h) or len(h) < 2:
            return False
        # 2 pointer issue. Left and right.

        i = 0
        j = len(h) - 1
        mx = 0

        while i < j:
            low = min(h[i], h[j])

            mx = max(mx, low * (j - i))

            while h[i] <= low and i < j:
                i += 1
            while h[j] <= low and i < j:
                j -= 1

        return mx


def build():
    return [1, 8, 6, 2, 5, 4, 8, 3, 7]


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea(build()))
