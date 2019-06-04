#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

Given an array of integers nums and a positive integer k,
find whether it's possible to
divide this array into k non-empty subsets whose sums are all equal.


Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation:
It's possible to divide it into 4 subsets
(5), (1, 4), (2,3), (2,3) with equal sums.


Note:
1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""


class Solution(object):
    def canPartitionKSubsets(self, A, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(A) < k:
            return False

        ASum = sum(A)
        if ASum % k != 0:
            return False

        # 大到小
        A.sort(reverse=True)

        # 限制條件: target即和除以k 故絕對滿足
        # 除非數目無法湊成 和/k 的值 不然一定可以符合


        target = [ASum / k] * k

        def dfs(pos):
            if pos == len(A): return True

            for i in xrange(k):
                if target[i] >= A[pos]:
                    target[i] -= A[pos]
                    if dfs(pos + 1):
                        return True
                    target[i] += A[pos]

            return False

        return dfs(0)

def build():
    return [4, 3, 2, 3, 5, 2, 1], 4


if __name__ == "__main__":
    s = Solution()
    print(s.canPartitionKSubsets(*build()))
