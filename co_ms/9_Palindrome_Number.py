#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/palindrome-number/description/

Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true


Example 2:
Input: -121
Output: false
Explanation:
From left to right, it reads -121.
From right to left, it becomes 121-. Therefore it is not a palindrome.


Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

***重要!!!
Coud you solve it without converting the integer to a string?
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        Idea:
        數字右往左建構一個新的數字. 即palindrom數字.
        若此新建構的數字與原數字相同 則為palindrom.
        """
        if x < 0:
            return False

        y = 0

        tmp = x

        while tmp:
            y *= 10
            y += tmp % 10
            tmp /= 10

        return y == x


def build():
    return 1000021
    return 1234567654321
    return 100001
    return 1


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(build()))
