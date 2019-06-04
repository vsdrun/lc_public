#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/integer-replacement/description/

Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.


What is the minimum number of replacements needed for n to become 1?

Example 1:
Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1

--------
Example 2:
Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1

or

7 -> 6 -> 3 -> 2 -> 1
"""
# https://discuss.leetcode.com/topic/58454/0-ms-c-recursion-solution-with-explanation


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 注意: 100 除盡的 減一, 為 11 也減一
        """
        100 - 1 = 011
        011 - 1 = 010
        010 > 001
        """
        rtn = 0

        while n > 1:
            rtn += 1

            print("on: {0}".format(n))
            # 如果為even, 先除二
            if n % 2 == 0:
                n = n >> 1
            elif (n + 1) % 4 or n == 3:
                print("n: {0}".format(n))
                n -= 1
            else:
                n += 1

        return rtn


def build_input():
    return 7


if __name__ == "__main__":
    input = build_input()

    s = Solution()
    result = s.integerReplacement(input)
    print(result)
