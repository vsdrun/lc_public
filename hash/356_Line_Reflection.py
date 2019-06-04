#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/line-reflection/description/


Given n points on a 2D plane,
find if there is such a line parallel to y-axis that reflect the given points.


Example 1:
Given points = [[1,1],[-1,1]], return true.

Example 2:
Given points = [[1,1],[-1,-1]], return false.

Follow up:
Could you do better than O(n^2)?

https://leetcode.com/problems/line-reflection/discuss/82967/C++-Beats-100-use-64-bit-int-to-hash-pair


思考:
    使用compliment概念.
    將2維以1維表示.
"""


class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        mn = float("inf")
        mx = float("-inf")

        result = set()

        for p in points:
            mn = min(mn, p[0])
            mx = max(mx, p[0])
            result.add(p[0] << 32 ^ p[1])

        compliment = mn + mx

        for p in points:
            compliment_x = compliment - p[0]
            y = p[1]
            r = compliment_x << 32 ^ y

            if r not in result:
                return False

        return True


def build():
    return [[1, 1], [1, 1], [1, 1]]
    return [[1, 1], [0, 0], [-1, 1]]
    return [[0, 0], [1, 0], [3, 0]]
    return [[1, 1], [-1, -1]]
    return [[1, 1], [-1, 1]]
    return [[0, 0], [1, 0]]


if __name__ == "__main__":
    s = Solution()
    print(s.isReflected(build()))
