#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers
such that they add up to the target, where index1 must be less than index2.


Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and
you may not use the same element twice.


Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # ascend order
        # 夾擠
        # using tilda? no, is not increasing/decrease in pair...

        bi = len(numbers) - 1
        fi = 0

        while fi < bi:
            summ = numbers[fi] + numbers[bi]

            if summ == target:
                return [fi + 1, bi + 1]
            if summ < target:
                fi += 1
            if summ > target:
                bi -= 1


def build():
    return [2, 7, 11, 15], 9


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum(*build()))
