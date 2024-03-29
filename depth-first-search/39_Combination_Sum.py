#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/combination-sum/

Given a set of candidate numbers (candidates) (without duplicates) and a
target number (target), find all unique combinations in candidates where the
candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]


Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        cc = candidates

        def backtrace(sol, startIdx, target):
            if target == 0:
                result.append(sol[:])
                return

            for i in range(startIdx, len(cc)):
                if target < cc[startIdx]:
                    break

                sol.append(cc[i])
                backtrace(sol, i, target - cc[i])
                sol.pop()

        backtrace([], 0, target)

        return result

def build():
    return [2, 3, 5], 8


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum(*build()))
