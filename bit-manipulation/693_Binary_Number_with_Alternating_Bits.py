#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/binary-number-with-alternating-bits/description/

Given a positive integer,
check whether it has alternating bits: namely,
if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101


Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.


Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
"""


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mask = 1
        expect = mask & n

        while n:
            if n & mask and expect:
                expect = False
                n >>= 1
                continue

            if not n & mask and not expect:
                expect = True
                n >>= 1
                continue

            return False

        return True


def build():
    result = 6
    return result


if __name__ == "__main__":
    s = Solution()
    result = s.hasAlternatingBits(build())
    print(result)
