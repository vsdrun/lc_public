#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/plus-one/description/

Given a non-empty array of digits representing a non-negative integer,
plus one to the integer.

The digits are stored such that the most significant digit is
at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero,
except the number 0 itself.


Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.


Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0

        for i in xrange(len(digits) - 1, -1, -1):
            result = digits[i] + carry + (1 if i == len(digits) - 1 else 0)
            digits[i] = result % 10
            carry = result / 10

        if carry:
            return [carry] + digits
        return digits

    def plusOne_fancy(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return map(int, list(str(int(''.join(map(str, digits))) + 1)))


def build():
    return [0]
    return [9, 9]
    return [4, 3, 2, 2]


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne(build()))
