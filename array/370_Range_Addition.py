#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/range-addition/description/


Assume you have an array of length n initialized with all 0's
and are given k update operations.

Each operation is represented as a triplet:
[startIndex, endIndex, inc] which increments each element of subarray
A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:
Given:

    length = 5,
    updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]
    ]

Output:
    [-2, 0, 3, 5, 3]



Explanation:

Initial state:
[ 0, 0, 0, 0, 0 ]

After applying operation [1, 3, 2]:
[ 0, 2, 2, 2, 0 ]

After applying operation [2, 4, 3]:
[ 0, 2, 5, 5, 3 ]

After applying operation [0, 2, -2]:
[-2, 0, 3, 5, 3 ]
"""


class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]

        思考:
        use the concept of accumulation.
        """
        rr = [0] * length

        for u in updates:
            # 注意是累加
            rr[u[0]] += u[2]

            if u[1] + 1 <= (length - 1):
                # 注意是 += -u[2]
                rr[u[1] + 1] += -u[2]

        summ = 0

        for i in range(length):
            # 注意是累加, carry on to next column
            summ += rr[i]
            rr[i] = summ

        return rr


def build():
    return 5, [[1, 3, 2],
               [2, 4, 3],
               [0, 2, -2]]


if __name__ == "__main__":

    s = Solution()
    print(s.getModifiedArray(*build()))
