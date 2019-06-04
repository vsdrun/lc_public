#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/monotonic-array/

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].
An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.


Example 1:
Input: [1,2,2,3]
Output: true

Example 2:
Input: [6,5,4,4]
Output: true

Example 3:
Input: [1,3,2]
Output: false

Example 4:
Input: [1,2,4,5]
Output: true

Example 5:
Input: [1,1,1]
Output: true

Note:
1 <= A.length <= 50000
-100000 <= A[i] <= 100000
"""


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        Increase = 0  # 1 increase, 2 decrease, 0 init.

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                if Increase == 0:
                    Increase = 1
                    continue
                elif Increase != 1:
                    return False

            if A[i] < A[i - 1]:
                if Increase == 0:
                    Increase = 2
                    continue
                elif Increase != 2:
                    return False

        return True



def build():
    return [1, 2, 5, 4, 4]
    return [1, 2, 3, 4, 4]
    return [1, 1, 1, 1, 1]
    return [1, 2, 3, 2, 1]
    return [4, 3, 2, 1, 1]


if __name__ == "__main__":
    s = Solution()
    print(s.isMonotonic(build()))
