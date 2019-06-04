#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/product-of-array-except-self/description/


Given an array of n integers where n > 1, nums,
return an array output such that output[i] is equal to
the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity?
(Note: The output array does not count as extra space for
the purpose of space complexity analysis.)
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        掃兩遍.
        第一遍由前往後 每個slot為前面的乘積.
        第二遍由後往前 每個slot為之前slot的值(即前面的乘積) 乘上 後面的乘積.
        第二遍掃完slot存放著結果.
        """
        p = 1
        n = len(nums)

        output = []

        for i in range(0, n):
            output.append(p)
            p = p * nums[i]

        p = 1

        for i in range(n - 1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]

        return output

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from __builtin__ import xrange

        # first scan

        result = [1]

        for i in xrange(1, len(nums)):
            result.append(result[-1] * nums[i - 1])

        back_result = 1

        for i in xrange(len(nums) - 2, -1, -1):
            back_result *= nums[i + 1]
            result[i] = result[i] * back_result

        return result

    def rewrite2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1]
        # [3, 7, 9 ,2 , 5]
        # left to right scan
        for idx in range(1, len(nums)):
            result.append(nums[idx - 1] * result[idx - 1])

        # right to left scan
        backResult = 1

        for idx in range(len(nums) - 2, -1, -1):
            backResult = backResult * nums[idx + 1]
            result[idx] = result[idx] * backResult

        return result


    def rewrite3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        return [1, 2, 3, 4]
        """

        # fwd
        tmp = [1] * len(nums)

        for idx in range(1, len(nums)):
            tmp[idx] = nums[idx - 1] * tmp[idx - 1]

        # bwd
        # 避免使用新的tmp, 利用一個variable存後端的乘積
        rightValue = 1
        for idx in range(len(nums) - 2, -1, -1):
            rightValue = nums[idx + 1] * rightValue
            tmp[idx] = tmp[idx] * rightValue

        return tmp



def build():
    return [1, 2, 3, 4]
    return [3, 7, 0, 5, 3, 1, 2, 6]
    return [3, 0, 2, 1]
    return [0, 0]


if __name__ == "__main__":

    s = Solution()
    print(s.productExceptSelf(build()))
    print(s.rewrite(build()))
    print(s.rewrite2(build()))
    print(s.rewrite3(build()))
