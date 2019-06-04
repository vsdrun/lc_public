#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-pivot-index/description/

Given an array of integers nums,
write a method that returns the "pivot" index of this array.

**
We define the pivot index as the index where the sum of the numbers
to the left of the index is equal to the sum of the numbers to
the right of the index.

If no such index exists, we should return -1.
If there are multiple pivot indexes,
**
you should return the left-most pivot index.

Example 1:
Input:
nums = [1, 7, 3, 6, 5, 6]
Output: 3

Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6)
is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.


Example 2:
Input:
nums = [1, 2, 3]
Output: -1

Explanation:
There is no index that satisfies the conditions in the problem statement.

Note:
The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].
"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        # build sum cache
        sums = []
        for n in nums:
            sums.append(sums[-1] + n if sums else n)

        for idx in range(len(nums)):
            if idx:
                if sums[idx - 1] == sums[-1] - sums[idx]:
                    return idx
            else:
                if 0 == sums[-1] - sums[idx]:
                    return idx

        return -1

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        sums = sum(nums)

        leftSum = 0

        for idx in range(len(nums)):

            if leftSum == (sums - (leftSum + nums[idx])):
                return idx

            leftSum += nums[idx]

        return -1

def build():
    return [1, 7, 3, 6, 5, 6]
    return [1]
    return [-1,-1,-1,0,1,1]

if __name__ == "__main__":
    print(Solution().pivotIndex(build()))
    print(Solution().rewrite(build()))
