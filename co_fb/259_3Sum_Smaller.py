#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/3sum-smaller/

Given an array of n integers nums and a target,
find the number of index triplets i, j, k with 0 <= i < j < k < n that
satisfy the condition nums[i] + nums[j] + nums[k] < target.


Example:
Input: nums = [-2,0,1,3], and target = 2
Output: 2

Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]

Follow up: Could you solve it in O(n^2) runtime?

"""


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        不能用累加 因為結果可以跳躍.
        i + j + k < t 則
        i + j-1 ... j + k < t
        i + i+1 ... k < t

        固定最左側 開始找解.
        """
        nums.sort()
        count = 0

        for k in range(len(nums)):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] < target:
                    count += (j - i)
                    i += 1
                else:
                    j -= 1

        return count


def build():
    return [-2, 0, 1, 3], 2


if __name__ == "__main__":
    s = Solution()
    print(s.threeSumSmaller(*build()))
