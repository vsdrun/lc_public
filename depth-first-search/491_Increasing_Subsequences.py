#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/increasing-subsequences/description/

Given an integer array,
your task is to find all the different possible increasing subsequences
of the given array,
and the length of an increasing subsequence should be at least 2 .


Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7],
         [6, 7], [6, 7, 7], [7,7], [4,7,7]]


Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates,
and two equal integers should also be considered as a
special case of increasing sequence.
"""


class Solution(object):

    def findSubsequences(self, nums):
        # First build all increasing subsequences regardless of length,
        # then filter out the too short ones.

        subs = {()}

        for num in nums:
            subs |= {sub + (num,)
                     for sub in subs
                     if not sub or sub[-1] <= num}

        return [sub for sub in subs if len(sub) >= 2]

    def rewrite(self, nums):
        # First build all increasing subsequences regardless of length,
        # then filter out the too short ones.

        subs = set([()])

        for num in nums:
            tmp_subs = set()

            for s in subs:
                if not s or s[-1] <= num:
                    tmp_subs.add(s + (num,))

            subs = subs | tmp_subs
        return [s for s in subs if len(s) >= 2]


def build():
    return [7, 3, 1, 9, 10]
    return [4, 6, 7, 7]


if __name__ == "__main__":
    s = Solution()
    print(s.findSubsequences(build()))
    print(s.rewrite(build()))
