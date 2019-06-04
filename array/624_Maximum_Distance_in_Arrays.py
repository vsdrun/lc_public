#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/maximum-distance-in-arrays/description/

Given m arrays, and each array is sorted in ascending order.
Now you can pick up two integers from two different arrays
(each array picks one) and calculate the distance.

We define the distance between two integers a and b to be their
absolute difference |a-b|. Your task is to find the maximum distance.


Example 1:
Input:
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4

Explanation:
One way to reach the maximum distance 4 is to pick 1 in the
first or third array and pick 5 in the second array.
"""


class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """

        res, curMin, curMax = 0, 10000, -10000

        for a in arrays:
            res = max(res, max(a[-1] - curMin, curMax - a[0]))
            curMin, curMax = min(curMin, a[0]), max(curMax, a[-1])

        return res


def build():
    return [[1, 2, 3],
            [4, 5],
            [1, 2, 3]]


if __name__ == "__main__":

    s = Solution()
    result = s.threeSum(build())
    print(result)
