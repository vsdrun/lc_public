#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/2-keys-keyboard/description/


Initially on a notepad only one character 'A' is present.
You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad
(partial copy is not allowed).

Paste: You can paste the characters which are copied last time.
Given a number n.

You have to get exactly n 'A' on the notepad by performing the minimum
number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:
Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Note:
The n will be in the range [1, 1000].
"""


class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        from __builtin__ import xrange

        dp = [99999999] * (n + 1)
        dp[0] = 1
        dp[1] = 0

        for current_cnt in xrange(1, n + 1):
            for start_cnt in xrange(1, current_cnt):

                left_cnt = current_cnt - start_cnt

                if not left_cnt % start_cnt:
                    copyable = 1

                    dp[current_cnt] = min(
                        dp[current_cnt],
                        dp[start_cnt] + copyable + left_cnt / start_cnt)
                    # + 1 is to copyall aka. copyable.

        return dp[n]


def build():
    return 5
    return 3
    return 2
    return 4
    return 1


if __name__ == "__main__":
    s = Solution()
    print(s.minSteps(build()))
