#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/

Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]


Given an array that is definitely a mountain,
return any i such that:
A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]


Example 1:
Input: [0,1,0]
Output: 1

Example 2:
Input: [0,2,1,0]
Output: 1

Note:
3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
"""


class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                return i - 1

    def rewrite_BinarySearch(self, A):
        """
        Better solution, O(log(N))
        """
        l, h = 0, len(A)-1

        while l < h:
            m = (l+h)/2

            if A[m] > A[m+1]:
                h = m
            else:
                l = m + 1

        return l



def build():
    return [0,1,3,6,2,1, 9, 10]
    return [0,1,0]


if __name__ == "__main__":
    s = Solution()
    print(s.peakIndexInMountainArray(build()))
