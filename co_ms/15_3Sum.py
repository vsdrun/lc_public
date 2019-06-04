#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/3sum/description/

Given an array S of n integers, are there elements a, b, c in S such
that a + b + c = 0?

Find all unique triplets in the array which gives the sum of zero.


Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        加起來為0 則一定要有負數.
        先排序 目的: 吃掉repeat的數字.
        先固定一個數字 然後算還需要那兩個數字.
        """
        from __builtin__ import xrange

        res = []

        # 排序吃子
        nums.sort()

        for i in xrange(len(nums) - 2):
            # eat repease char.
            if i and nums[i] == nums[i - 1]:
                continue

            s = i + 1
            e = len(nums) - 1

            while s < e:
                # nums[i] 固定.
                # 其後的 s / e 為排序過的.
                summ = nums[i] + nums[s] + nums[e]

                if summ < 0:
                    s += 1
                elif summ > 0:
                    e -= 1
                else:
                    res.append((nums[i], nums[s], nums[e]))

                    # 吃掉重複
                    while s < e and nums[s] == nums[s + 1]:
                        s += 1
                    # 吃掉重複
                    while s < e and nums[e] == nums[e - 1]:
                        e -= 1

                    s += 1
                    e -= 1

        return res

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from __builtin__ import xrange

        # sort to avoid duplicate
        nums.sort()

        result = []

        # be aware the range boundary!
        # 保留最後兩個 for calculation!
        for i in xrange(len(nums) - 2):

            if i and nums[i] == nums[i - 1]:
                continue

            s_idx = i + 1
            e_idx = len(nums) - 1

            while s_idx < e_idx:
                ssum = nums[i] + nums[s_idx] + nums[e_idx]

                if ssum < 0:
                    s_idx += 1
                elif ssum > 0:
                    e_idx -= 1
                else:
                    result.append([nums[i], nums[s_idx], nums[e_idx]])
                    s_idx += 1
                    e_idx -= 1

                    while s_idx < e_idx:
                        if nums[s_idx] == nums[s_idx - 1]:
                            s_idx += 1
                            continue
                        break

                    while s_idx < e_idx:
                        if nums[e_idx] == nums[e_idx + 1]:
                            e_idx -= 1
                            continue
                        break

        return result

    def rewrite2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],
[-4, -1, -1, 0 , 1 , 2]

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
        """
        if not nums:
            return []

        nums.sort()
        result = []

        # 用for loop來定pivot
        for idx in range(len(nums) - 2):
            # idx == 0 一定要 作為起始阿...
            # pivot 重複的先跳過. 記得 是pivot重複跳過...
            if idx and nums[idx] == nums[idx - 1]:
                continue

            summ = 0
            sidx = idx + 1
            eidx = len(nums) - 1

            while sidx < eidx:
                summ = nums[idx] + nums[sidx] + nums[eidx]

                if summ < 0:
                    sidx += 1
                elif summ > 0:
                    eidx -= 1
                else:
                    result.append([nums[idx], nums[sidx], nums[eidx]])

                    while sidx < eidx and nums[sidx] == nums[sidx+1]:
                        sidx += 1
                    sidx += 1

                    while sidx < eidx and nums[eidx] == nums[eidx-1]:
                        eidx -= 1
                    eidx -= 1

        return result


def build():
    return [-1, 0, 1, 2, -1, -4]
    return [-1, 0, 1, 2, -1]
    return [-1, 0, 1, 2, -1, -4]
    return [0, 0, 0, 0]
    return [0, 0, 0]


if __name__ == "__main__":

    s = Solution()
    print(s.threeSum(build()))
    print(s.rewrite(build()))
    print(s.rewrite2(build()))
