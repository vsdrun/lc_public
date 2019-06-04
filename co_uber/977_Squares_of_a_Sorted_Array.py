#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/squares-of-a-sorted-array/

Given an array of integers A sorted in non-decreasing order,
return an array of the squares of each number, also in sorted non-decreasing order.


Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]


Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Note:
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        lidx = 0
        ridx = len(A) - 1

        while lidx <= ridx:
            if abs(A[lidx]) > abs(A[ridx]):
                result.append(A[lidx]**2)
                lidx += 1
            else:
                result.append(A[ridx]**2)
                ridx -= 1

        return result[::-1]




def build():
    return [0,2]
    return [-1,1]
    return [-7,-3,2,3,11]


if __name__ == "__main__":
    s = Solution()
    print(s.sortedSquares(build()))
    print(s.rewrite(build()))
