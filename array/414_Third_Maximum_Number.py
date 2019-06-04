#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/third-maximum-number/description/


Given a non-empty array of integers,
return the third maximum number in this array.
If it does not exist, return the maximum number.
The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        negative = -9999999999999999999999999999999999999999999
        mx1 = mx2 = mx3 = negative

        for n in nums:
            if n > mx1:
                mx1, mx2, mx3 = n, mx1, mx2
            elif mx1 > n > mx2:
                mx2, mx3 = n, mx2
            elif mx2 > n > mx3:
                mx3 = n

        return mx3 if mx3 != negative else mx1


def build():
    return [2, 2, 3, 1]


if __name__ == "__main__":
    s = Solution()
    print(s.thirdMax(build()))
