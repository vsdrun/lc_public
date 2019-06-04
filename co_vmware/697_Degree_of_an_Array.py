#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/degree-of-an-array/

Given a non-empty array of non-negative integers nums,
the degree of this array is defined as the maximum frequency of any
one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray
of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""


class Solution(object):
    def findShortestSubArray(self, nums):

        first, counter, res, degree = {}, {}, 0, 0

        for i, v in enumerate(nums):
            first.setdefault(v, i)
            counter[v] = counter.get(v, 0) + 1

            if counter[v] > degree:
                degree = counter[v]
                res = i - first[v] + 1
            elif counter[v] == degree:
                res = min(res, i - first[v] + 1)

        return res


def build():
    return [1, 2, 2, 3, 1]


if __name__ == "__main__":
    s = Solution()
    print(s.findShortestSubArray(build()))
