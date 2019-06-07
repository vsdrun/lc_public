#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        cc = candidates
        cc.sort()

        def dfs(idx, cresult, residule):
            if residule == 0:
                result.append(cresult[:])
                return

            for i in range(idx, len(cc)):
                if cc[i] > residule:
                    break

                if i > idx and cc[i] == cc[i-1]:
                    continue

                cresult.append(cc[i])
                dfs(i + 1, cresult, residule - cc[i])
                cresult.pop()

        dfs(0, [], target)
        return result


def build():
    # 1, 1, 2, 5, 6, 7, 10
    return [10,1,2,7,6,1,5], 8
    #  [
      #  [1, 7],
      #  [1, 2, 5],
      #  [2, 6],
      #  [1, 1, 6]
    #  ]


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2(*build()))
