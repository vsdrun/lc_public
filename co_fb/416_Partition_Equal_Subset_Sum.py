#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that the
sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.

Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].


Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592/01-knapsack-detailed-explanation
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        概念 總和 / 2 的值為target.
        """
        ss = sum(nums)

        if ss & 1 == 0: # 如果是2的倍數才處理.
            target = ss >> 1  # 總和 / 2
            cur = {0}

            for i in nums:
                cur |= {i + x for x in cur}  # 每個和都檢查其值是否與target同
                if target in cur:
                    return True

        return False

    def rewritedp(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        概念 總和 / 2 的值為target.
        """
        ss = sum(nums)
        if ss & 1:
            return False

        half = ss/2
        dp = [False] * (half + 1)
        dp[0] = True

        # [T, F, F, F, F, F, F, F, F, F, F, F]  // 11
        for n in nums:
            for idx in range(len(dp) - 1, -1, -1):
                #  print("idx: {}".format(idx))
                if idx >= n:
                    dp[idx] = dp[idx] or dp[idx - n]

        return dp[len(dp)-1]

def build():
    return [4, 5, 11, 5]
    return [1, 5, 11, 5]


if __name__ == "__main__":
    s = Solution()
    print(s.canPartition(build()))
    print(s.rewritedp(build()))
