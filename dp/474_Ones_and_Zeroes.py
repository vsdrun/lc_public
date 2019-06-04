#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/ones-and-zeroes/description/

For now, suppose you are a dominator of m 0s and n 1s respectively.
On the other hand, there is an array with strings consisting
of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with
given m 0s and n 1s. Each 0 and 1 can be used at most once.

輸入:
1. m 個 0
2. n 個 1
3. array of string: string[]
條件:
每個0,1只能用一次
需求:
找出所有strings in string[] 其可以用m個0與n個1組成
若一string用掉的0,1便是用掉了，剩下的給其他strings match.
找出最多可以match的strings(用掉所有0,1)

Note:
The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.

Example 1:
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s
and 3 1s, which are “10,”0001”,”1”,”0”


Example 2:
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left.
Better form "0" and "1".
"""


class Solution(object):

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int 0
        :type n: int 1
        :rtype: int
        """
        """
        每一個DP均為獨立事件.
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        def count(s):
            return (sum(1 for c in s if c == '0'),
                    sum(1 for c in s if c == '1'))

        for zeros, ones in [count(s) for s in strs]:
            for mi in range(m, -1, -1):
                for ni in range(n, -1, -1):
                    if mi >= zeros and ni >= ones:
                        dp[mi][ni] = max(1 + dp[mi - zeros][ni - ones],
                                         dp[mi][ni])

        return dp[m][n]


def build_input():
    return ["10", "0001", "111001", "1", "0"], 5, 3


if __name__ == "__main__":
    strs, m, n = build_input()

    s = Solution()
    result = s.findMaxForm(strs, m, n)

    print(result)
