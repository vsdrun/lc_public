#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/decode-ways/description/

A message containing letters from A-Z is being encoded
to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits,
determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        dp = [0 for x in range(len(s) + 1)]
        dp[0] = 1  # 重要!!! 帶到下一個進入點

        for i in range(1, len(s) + 1):
            if s[i - 1] != "0":  # 指此slot, 即目前process的char.
                dp[i] += dp[i - 1]  # 此slot + 之前slot的值
                # 更重要的是 若前一個dp為0, 則此dp也為0! invalid input!
            if i != 1 and s[i - 2:i] < "27" and s[i - 2:i] > "09":
                dp[i] += dp[i - 2]  # e.g 2,21:

        return dp[len(s)]


def build():
    return "234"


if __name__ == "__main__":

    s = Solution()
    print(s.numDecodings(build()))
