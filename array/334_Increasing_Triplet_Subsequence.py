#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/increasing-triplet-subsequence/description/

Given an unsorted array return whether an increasing subsequence
of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
"""


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        沒有要求要連續!
        只要有三個 持續上揚的數即可..
        """
        first = second = float('inf')

        for n in nums:
            if n <= first:
                first = n
            elif n < second:
                second = n
            else:
                return True

        return False


def build():
    return [3, 2, 3, 2, 4, 5]
    return [1, 1, -2, 6]
    return [1, 2, 1, 3, 2]
    return [5, 1, 5, 5, 2, 5, 4]
    return [1, 7, 1, 2, 5]
    return [1, 2, 3, 4, 5]


if __name__ == "__main__":

    s = Solution()
    print(s.increasingTriplet(build()))
