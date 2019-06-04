#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/interval-list-intersections/

Given two lists of closed intervals,
each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real
numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that is
either empty, or can be represented as a closed interval.

For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder:
The inputs and the desired output are lists of Interval objects,
and not arrays or lists.

Note:
0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
NOTE:
input types have been changed on April 15, 2019.
Please reset to default code definition to get new method signature.
"""

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        O(M*N)
        """
        result = []

        for a in A:
            al, ar = a[0], a[1]

            for b in B:
                bl, br = b[0], b[1]
                if bl > ar:
                    break
                if br < al:
                    continue

                l = max(al, bl)
                r = min(ar, br)
                result.append([l, r])

        #  [[1, 5], [10, 12], [15, 23], [24, 24], [25, 25]]
        return result

    def rewrite(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        O(M+N)
        """
        i = 0
        j = 0
        result = []

        while i < len(A) and j < len(B):
            if A[i][1] < B[j][0]:
                i += 1
                continue
            elif B[j][1] < A[i][0]:
                j += 1
                continue

            l = max(A[i][0], B[j][0])
            r = min(A[i][1], B[j][1])
            result.append([l, r])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return result

def build():
    A = [[0, 7],[10, 12],[13,23],[24,25]]
    B = [[1,5],[8,12],[15,24],[25,26]]
    # [1, 5] [10, 12] [15, 23] [25]
    #  Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    return A, B
    A = [[0,2],[5,10],[13,23],[24,25]]
    B = [[1,5],[8,12],[15,24],[25,26]]
    #  Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    #  [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    return A, B

if __name__ == "__main__":
    s = Solution()
    print(s.intervalIntersection(*build()))
    print(s.rewrite(*build()))
