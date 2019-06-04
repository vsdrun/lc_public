#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/can-i-win/description/

In the "100 game," two players take turns adding, to a running total,
any integer from 1..10.
The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players **cannot** re-use integers?

For example,
two players might take turns drawing from a common pool of numbers of 1..15
without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal,
determine if the first player to move can force a win,
assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger
than 20 and desiredTotal will not be larger than 300.


Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.

If the first player choose 1, the second player can
only choose integers from 2 up to 10.

The second player will win by choosing 10 and get a total = 11,
which is >= desiredTotal.

Same with other integers chosen by the first player,
the second player will always win.
"""


class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        from __builtin__ import xrange

        # check if input's valid.
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False

        # early filter
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 == desiredTotal:
            return bool(maxChoosableInteger % 2)

        nums = range(1, maxChoosableInteger + 1)

        def recursive(nums, desired, memoir):
            hash = str(nums)

            if hash in memoir:
                return memoir[hash]

            if nums[-1] >= desired:
                # 這一手便贏了!
                return True

            for i in xrange(len(nums)):
                # 現在這個local snapshot 看我要以此nums[i] 為起手.
                # 期望下面的Fail 則此local贏!
                if not recursive(
                        nums[:i] + nums[i + 1:], desired - nums[i], memoir):
                    memoir[hash] = True
                    return True

                memoir[hash] = False

            return False

        return recursive(nums, desiredTotal, dict())

    def canIWin_2(self, x, t):

        n = x * (x + 1) / 2

        if n < t:
            return False
        elif n == t:
            return bool(x % 2)

        s, m = range(x, 0, -1), {}

        def dfs(t, a):
            if a in m:
                return m[a]

            for x in s:
                i = 1 << (x - 1)
                if a & i:
                    if t <= x or not dfs(t - x, a ^ i):
                        r = True
                        break
            else:
                r = False

            m[a] = r

            return r

        # bit manipulation.
        return dfs(t, 2**(x + 1) - 1)


def build():
    return 5, 10
    return 10, 11
    return 10, 20


if __name__ == "__main__":
    s = Solution()
    print(s.canIWin(*build()))
