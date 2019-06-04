#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/burst-balloons/


Given n balloons, indexed from 0 to n-1.

Each balloon is painted with a number on it represented by array nums.

You are asked to burst all the balloons.
If the you burst balloon i you will get
nums[left] * nums[i] * nums[right] coins.

Here left and right are adjacent indices of i. After
the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.


Note:
(1) You may imagine nums[-1] = nums[n] = 1.
    They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100


Example:
Given [3, 1, 5, 8]
Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""


class Solution(object):

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        1. 夾擠. 總coins和 == [0 , k, n] + [0, x, k] + [k, y, n]
        2. 也就是，若要算[0,k,n] 則表示 0~k中間已經被pop掉,而我們要最大的.
        3. k~n中間也被pop掉，我們要最大的.
        3. 有 左右上下限時，create matrix(m*n) m as 左限, n as 右限.
        """
        from __builtin__ import xrange
        nums = [1] + nums + [1]
        n = len(nums)

        # 為matrix
        dp = [[0] * n for _ in xrange(n)]

        def calculate(i, j):
            # i, j are inclusive.
            if dp[i][j] or j == i + 1:  # j == i + 1 表示i,j相鄰.
                return dp[i][j]

            coins = 0

            # 此 for loop 表示 不含i 不含j
            for k in xrange(i + 1, j):  # find the last balloon
                coins = max(
                    coins,
                    nums[i] * nums[k] * nums[j] + calculate(i,
                                                            k) + calculate(k,
                                                                           j))

            dp[i][j] = coins
            return coins

        return calculate(0, n - 1)  # [0, n-1] , it's index.

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        1. 解決 subproblem
        2. range:
        1 x 1, 1 與 x  之間的要全部pop掉.
        """
        from __builtin__ import xrange

        nums = [1] + nums + [1]
        n_len = len(nums)

        # create dp matrix
        dp = [[0] * n_len for _ in xrange(n_len)]

        def count(i, j):

            if dp[i][j] or i + 1 == j:
                return dp[i][j]

            for k in xrange(i + 1, j):
                summ = nums[i] * nums[k] * nums[j]
                dp[i][j] = max(dp[i][j], summ + count(i, k) + count(k, j))

            return dp[i][j]

        return count(0, n_len - 1)


def build():
    return [3, 1, 5, 8]


if __name__ == "__main__":
    s = Solution()

    result = s.maxCoins(build())
    print(result)

    result = s.rewrite(build())
    print(result)
