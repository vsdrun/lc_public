#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/4sum/

Given an array nums of n integers and an integer target, are there elements
a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        使用 len(nums) - N, where N == 4
        """

        def findNSum(lidx, ridx, N, target, result):
            # early exist...
            if (ridx - lidx + 1) < N or N < 2 or target < nums[lidx] * N or \
                target > nums[ridx] * N:
                return

            if N != 2:
                for idx in range(lidx, ridx + 1):
                    # 忽略重複的
                    # 因為重複的在下一個recursive call 會call 到
                    # 在此不須重複call...
                    if idx == lidx or nums[idx] != nums[idx - 1]:
                        findNSum(idx + 1, ridx, N - 1, target - nums[idx],
                                result + [nums[idx]])
            else:
                # N == 2
                while lidx < ridx:
                    s = nums[lidx] + nums[ridx]

                    if s == target:
                        final_result.append(
                            result + [nums[lidx]] + [nums[ridx]])
                        # 仍要繼續前進方可跳脫while loop
                        lidx += 1
                        # 吃掉重複的!
                        # 因為在上一個recursive call 會call到重複的於此call
                        # stack!
                        while lidx < ridx and nums[lidx] == nums[lidx - 1]:
                            lidx += 1

                    elif s < target:
                        lidx += 1
                    else:
                        ridx -= 1


        final_result = []
        nums.sort()  # always sorted.

        findNSum(0, len(nums) - 1, 4, target, [])

        return final_result

    def rewrite(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        pass~~~
        """
        if len(nums) < 4:
            return []

        nums.sort()

        if target < nums[0] * 4:
            return []

        fresult = []
        result = []

    #  return [-3, -2, -1, 0, 0, 1, 2, 3], 0
    #  return [1, 0, -1, 0, -2, 2], 0

        def sum2(nums, target):
            b = 0
            e = len(nums) - 1

            while b < e:
                if b > 0 and nums[b] == nums[b-1]:
                    b += 1
                    continue

                s = nums[b] + nums[e]

                if s == target:
                    fresult.append(result[:] + [nums[b], nums[e]])
                    b += 1

                if s > target:
                    e -= 1
                elif s < target:
                    b += 1


        def recursive(nums):
            if len(result) == 2:
                # 只需要兩個拉! 也就是可以做binary search
                t = target - sum(result)
                sum2(nums, t)
                return

            for idx in range(len(nums)):
                if idx > 0 and nums[idx] == nums[idx - 1]:
                    continue

                result.append(nums[idx])

                if len(result) == 4 and sum(result) == target:
                    fresult.append(result[:])

                recursive(nums[idx+1:])

                result.pop()

        recursive(nums)

        return fresult


"""
[[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
---
[[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
"""

def build():
    return [-3, -2, -1, 0, 0, 1, 2, 3], 0
    return [1, 0, -1, 0, -2, 2], 0
    return [0, 0, 0, 0], 0


if __name__ == "__main__":
    s = Solution()
    print(s.fourSum(*build()))
    print("---")
    print(s.rewrite(*build()))
