#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/permutations/description/

Given a collection of numbers that might contain duplicates,
return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):
    def permuteUnique(self, nums):
        from __builtin__ import xrange

        ans = [[]]

        for n in nums:
            new_ans = []

            for l in ans:
                for i in xrange(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])

                    print("new_ans :{}".format(new_ans))

                    if i < len(l) and l[i] == n:
                        break  # handles duplication

            ans = new_ans
        return ans

    def rewrite(self, nums):
        nums.sort()

        def recursive(nums):
            """
            :ret: list of list
            """
            result = []

            for i, v in enumerate(nums):
                if i and nums[i] == nums[i - 1]:
                    continue
                ret = [v]

                deep = recursive(nums[:i] + nums[i + 1:])

                for d in deep:
                    result.append(ret + d)

            return result if result else [[]]

        return recursive(nums)

    def rewrite2(self, nums):
        #  handles duplicate
        ans = [[]]

        for n in nums:
            tmp_ans = []

            for a in ans:
                for i in range(len(a) + 1):
                    tmp_ans.append(a[:i] + [n] + a[i:])

                    # 避免重複
                    if i < len(a) and a[i] == n:
                        break

            ans = tmp_ans
        return ans


def build():
    return [1, 1, 2]


if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique(build()))
    print(s.rewrite(build()))
    print(s.rewrite2(build()))
