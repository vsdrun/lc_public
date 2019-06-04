#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/patching-array/description/

Given a sorted positive integer array nums and an integer n, add/patch
elements to the array such that any number in range[1, n] inclusive can
be formed by the sum of some elements in the array.

Return the minimum number of patches required.


Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3],
which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are:
[1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
Return 0.
"""


class Solution(object):

    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        # 一定要有1, 因為 1 ~ n 必須含有1
        # missing 代表 1 ~ n 內沒有的數字
        # 表示[0,n]之间最小的不能表示的值
        missing = 1

        # 加多少數字
        adding = 0

        # travel through nums
        index = 0

        # 加入哪些數字
        result = []

        while missing <= n:
            if index < len(nums) and nums[index] <= missing:
                # 能表示的數擴大至 missing + nums[index]
                # 代表 [0~missing) 每個數字 + nums[index] 均能表達
                missing += nums[index]  # -- 1
                index += 1
            else:
                # 先至此 由 1 開始
                # 代表此刻 [1 ~ missing)都可以被表達出來
                result += missing,
                # 但是 missing本身無法被表達 所以加入 missing
                missing += missing  # 與 -- 1 同一logic.
                adding += 1

        print(result)

        return adding


def build_input():
    return [3, 4, 6, 9, 11, 13]


if __name__ == "__main__":
    n = build_input()

    s = Solution()
    result = s.minPatches(n, 5000)

    print(result)
