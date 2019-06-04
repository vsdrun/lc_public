#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/4-keys-keyboard/description/


Imagine you have a special keyboard with the following keys:

Key 1: (A): Print one 'A' on screen.

Key 2: (Ctrl-A): Select the whole screen.

Key 3: (Ctrl-C): Copy selection to buffer.

Key 4: (Ctrl-V): Print buffer on screen appending it
after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys),
find out the maximum numbers of 'A' you can print on screen.

Example 1:
Input: N = 3
Output: 3
Explanation:
We can at most get 3 A's on screen by pressing following key sequence:
A, A, A


Example 2:
Input: N = 7
Output: 9
Explanation:
We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
"""


class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        from __builtin__ import xrange

        dp = [0] * (N + 1)
        dp[1] = 1

        # buttom up
        for n in xrange(1, len(dp)):
            if n - 3 > 1:
                for i in xrange(1, (n - 3) + 1):
                    # 即 i 之後有 select A, copy A, 最後 past A
                    # 所以 i + 2
                    cnt = n - (i + 2) + 1

                    dp[n] = max(dp[n], dp[i] * cnt)

            dp[n] = max(dp[n], dp[1] * n)
        return dp[n]


def build():
    return 7
    return 3
    return 5
    return 100
    return 2
    return 1


if __name__ == "__main__":
    s = Solution()
    print(s.maxA(build()))
