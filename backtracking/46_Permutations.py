#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/permutations/description/

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

XD
list(itertools.permutations(nums))
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i + 1:])] or [[]]

    def permute_2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from __builtin__ import xrange

        perms = [[]]

        for n in nums:
            new_perms = []

            for perm in perms:
                for i in xrange(len(perm) + 1):
                    new_perms.append(perm[:i] + [n] + perm[i:])  # insert n

            perms = new_perms
        return perms

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def recursive(nums):
            ret = []
            for i, v in enumerate(nums):
                result = [v]

                # list of list
                deep = recursive(nums[:i] + nums[i + 1:])

                for d in deep:
                    ret.append(result + d)

            return ret if ret else [[]]

            """
            return [[v] + recursive(nums[:i] + nums[i + 1:])
                    for i, v in enumerate(nums)]
            """

        return recursive(nums)


def build():
    return [1, 2, 3]


if __name__ == "__main__":
    s = Solution()
    print(s.permute(build()))
    print(s.rewrite(build()))
