#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/contains-duplicate/description/


Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least
twice in the array,
and it should return false if every element is distinct.

"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

    def containsDuplicate_slow(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import collections as cc

        result = cc.Counter(nums)
        result = result.most_common()
        return False if not result or result[0][1] == 1 else True


def build():
    return [0]
    return []
    return [9, 3, 15, 20, 3, 7]


if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate(build()))
