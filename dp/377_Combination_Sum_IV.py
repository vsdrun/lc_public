#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/combination-sum-iv/description/

Given an integer array with all positive numbers and no duplicates, find the
number of possible combinations that add up to a positive integer target.

array內的數字可以重複使用來加總成target.

Example:
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""

"""
差一個數字便圓滿的概念.
即 secret + nums[i] = target
那麼, nums[i] 由幾個組成?
將所有的nums[i] 加總 便是 target可由幾個i組成.
think as DP.

注意!
每個 dp[i] 為獨立事件，也就是成就了題目所言:
(1,1,2) (1,2,1) 為不同的結果.

之所以用t - num[i]原因:
1. compliment. 也就是t - num[i] 這個數剩下的是否在nums list裡
若有，則代表可以num[i] + nums[t-i] 可以組成 t
若無，則nums[t-i]為0
以因此需從1 ~ t 逐項找.
"""


class Solution(object):

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        from __builtin__ import xrange

        # !!! prepare DP matrix
        dp = [0] * (target + 1)

        # dp 總有個初始化..
        dp[0] = 1  # 目的只是carry on to next dp[i], dp[0]為dummy entry.

        for t in xrange(1, target + 1):
            # t 代表 累進和到target的一個值
            # e.g target = 4, 則 t = 1,2,3,4
            # 也就是，target 為1時有幾種方法, 2時幾種, 3時幾種, 4時幾種.
            for n in nums:
                if t >= n:
                    dp[t] += dp[t - n]

        return dp[target]


def build():
    return [3, 2, 1], 4
    return [7, 2], 4
    return [1, 2, 3], 4


if __name__ == "__main__":
    s = Solution()
    result = s.combinationSum4(*build())

    print(result)
