#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/hamming-distance/description/

The Hamming distance between two integers is the number of
positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.


Example:
Input: x = 1, y = 4
Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        return bin(x ^ y).count('1')


def build():
    return 4, 9


if __name__ == "__main__":

    s = Solution()
    result = s.hammingDistance(*build())
    print(result)
