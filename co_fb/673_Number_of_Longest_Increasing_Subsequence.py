#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/number-of-longest-increasing-subsequence/

Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation:
The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation:
The length of longest continuous increasing subsequence is 1,
and there are 5 subsequences' length is 1, so output 5.

Note:
Length of the given array will be not exceed 2000 and the answer is
guaranteed to be fit in 32-bit signed int.
"""



class Solution(object):
    def countMaxSolution(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmplist = list()

        maxSize = 0
        cnt = 1

        for n in nums:
            right = len(tmplist) - 1
            left = 0

            while tmplist and left <= right:
                m = (right + left) / 2

                if tmplist[m] < n:
                    left = m + 1  # length + 1
                else:
                    right = m - 1

            if left > len(tmplist) - 1:
                tmplist.append(n)
                maxSize = len(tmplist)
                cnt = cnt

                print("tmplist in left add: {} cnt: {}".format(tmplist, cnt))
            else:
                tmplist[left] = n

                print("tmplist : {} cnt: {}".format(tmplist, cnt))

        return cnt


    def rewrite(self, nums):
        if nums == []:
            return 0

        # LIS 是長度
        # cnt 為此長度有多少個
        LIS, cnt = [1] * len(nums), [1] * len(nums)

        # [1, 3, 5, 4, 7]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if LIS[i] == LIS[j] + 1:
                        cnt[i] += cnt[j]
                    elif LIS[i] < LIS[j] + 1:
                        cnt[i] = cnt[j]
                        LIS[i] = LIS[j] + 1

        print("LIS: {}".format(LIS))
        print("cnt: {}".format(cnt))

        result = []

        for x, y in zip(LIS, cnt):
            print("{}, {}, MAX: {}".format(x, y, max(LIS)))

            if x == max(LIS):
                result.append(y)

        print(result)

        return sum(result)
        # 1 3 5 4 7
        # 1 2 3 3 4  MAX(4)  LIS  是長度.
        # 1 1 1 1 2   CNT   是這個長度有多少個.

def build():
    return [1, 3, 5, 4, 7]
    return [6, 7, 8, 2, 3, 4]
    return [1, 3, 5, 4]
    return [1, 3, 5]
    return [1, 3, 5, 4, 7]
    return [1, 2, 4, 3, 5, 4, 7, 2]
    return [1, 3, 5, 7]
    return [2, 2, 2, 2, 2]

if __name__ == "__main__":
    s = Solution()
    print(s.rewrite(build()))
