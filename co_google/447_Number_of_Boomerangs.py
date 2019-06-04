#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/number-of-boomerangs/description/

Given n points in the plane that are all pairwise distinct,
a "boomerang" is a tuple of points (i, j, k) such that the
distance between i and j equals the distance between i and k
(the order of the tuple matters).

Find the number of boomerangs.

You may assume that n will be at most 500 and
coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""


class Solution(object):

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        """
        Permutation:
        P(n,2) = n! / (n-2)! = n*(n-1)

        以下，若dt只有
        p1,p21, 夠不成boomerangs, 故count += h.get(dt,0) 為0
        而 若有 p1,p21 p1, p22 則為1

        而0,1 的和為 ((上底+下底)*n)/2 => (1*2)/2 => (n*(n-1))/2

        *** 聰明!!!
        而我們需要的P(n,2) 為 n*(n-1), 故次處多除了2

        最後的和 *2 成為 n*(n-1) => P(n,2)

        附註:
        C(n,d) = n!/(n-d)!d! // 除去排列
        P(n,d) = n!/(n-d)!
        """
        count = 0

        for i in range(len(points)):
            h = {}

            for j in range(len(points)):
                if i != j:
                    dt = pow(points[i][0] - points[j][0], 2) + \
                        pow(points[i][1] - points[j][1], 2)

                    count += h.get(dt, 0)
                    h[dt] = h.get(dt, 0) + 1

        return count * 2  # 因為排列


def build_input():
    return [[0, 0], [1, 0], [2, 0], [1, 1]]


if __name__ == "__main__":
    p = build_input()
    r = Solution()
    result = r.numberOfBoomerangs(p)
    print(result)
