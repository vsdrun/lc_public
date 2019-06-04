#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/next-greater-element-iii/

Given a positive 32-bit integer n,
you need to find the smallest 32-bit integer which has exactly the
same digits existing in the integer n and is greater in value than n.

If no such positive 32-bit integer exists, you need to return -1.

由既有的數字中找大下一個比此數大的數.

Example 1:
Input: 12
Output: 21


Example 2:
Input: 21
Output: -1
"""



class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int

        Idea:
        From back to forward:
        1 2 4 3 2 1
        """
        s = list(map(int, str(n)))

        l = len(s) - 1

        while l - 1 >= 0 and s[l] <= s[l - 1]:
            l -= 1

        j = l

        if l == 0:
            return -1

        while j + 1 <= len(s) - 1 and s[l - 1] < s[j + 1]:
            j += 1


        s[l-1] , s[j] = s[j], s[l-1]
        s[l:] = reversed(s[l:])  # 注意此

        result = int("".join(map(str, s)))

        return result if result <= ((1 << 31) - 1) else -1


def build():
    return 12222333  # 12223233  # 12223332
    return 230241
    return 124321
    return 12


if __name__ == "__main__":
    s = Solution()
    print(s.nextGreaterElement(build()))
