#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
You are given a list of non-negative integers, a1, a2, ..., an,
and a target, S. Now you have 2 symbols + and -.
For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers
equal to target S.


Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3


There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
1. The length of the given array is positive and will not exceed 20.
2. The sum of elements in the given array will not exceed 1000.
3. Your output answer is guaranteed to be fitted in a 32-bit integer.
"""


class Solution(object):

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        """
        DFS + cache
        """
        cache = {}

        def findTarget(index, s):
            if (index, s) not in cache:
                # result == 0
                result = 0

                if index == len(nums):
                    if s == 0:
                        result = 1
                else:
                    result = findTarget(index + 1, s - nums[index]) + \
                        findTarget(index + 1, s + nums[index])

                cache[(index, s)] = result

            return cache[(index, s)]

        return findTarget(0, S)

    def fast(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int

思路：
1、DFS：这道题目如果用DFS求解是最直观的。也可以通过，但是效率比较低，
因为其运行的时间复杂度是指数级的。

2、DP：该问题等价于：将nums中的元素划分为子集P和N，其中P中的元素都保持原值，
而N中的元素都取相反数，并且P和N中的元素之和为target。
例如给定nums = [1, 2, 3, 4, 5]并且target = 3.
那么一个可能的结果就是 +1-2+3-4+5 = 3。这里P = [1, 3, 5]，N = [2, 4]。
那么我们看看这个题目可以如何被转化为子集和问题：

                  sum(P) - sum(N) = target
sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
                       2 * sum(P) = target + sum(nums)

这样，问题就转换为如何在nums中找到一个子集P，
使得sum(P) = (target + sum(nums)) / 2。

需要注意到只有target + sum(nums)为偶数才有解，
所以我们可以在问题的开始阶段就检测一下。
该算法的时间复杂度为O(target * n)，其中n是nums中元素的个数。
        """
        def findSum(nums, S):
            dp = [1]+[0]*S

            for i in range(len(nums)):
                cur = nums[i]
                for val in range(S-cur, -1, -1):
                    if dp[val]:
                        dp[val+cur] += dp[val]
            return dp[S]

        sum_nums = sum(nums)

        if sum_nums < S:
            return 0

        if (sum_nums+S) % 2 != 0:
            return 0

        target = (sum_nums+S)/2

        return findSum(nums, target)

    def rewrite(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        """
        DFS + cache
        """
        memoir = dict()  # (idx,sum)
        tlen = len(nums)

        def dfs(idx, ssum):
            """
            :ret: int as accumulated result.
            """
            result = 0

            if (idx, ssum) not in memoir:
                if idx == tlen:  # 注意.
                    if ssum == 0:
                        result = 1  # 重要! 如果sum不為0 則result = 0
                else:
                    result = \
                        dfs(idx + 1, ssum + nums[idx]) + \
                        dfs(idx + 1, ssum - nums[idx])

                memoir[(idx, ssum)] = result  # result 為 0 if sum != 0

            return memoir[(idx, ssum)]

        return dfs(0, S)


def build_input():
    return [1, 1, 1, 1, 1], 3


if __name__ == "__main__":
    s = Solution()
    print(s.findTargetSumWays(*build_input()))
    print(s.rewrite(*build_input()))
    print(s.fast(*build_input()))
