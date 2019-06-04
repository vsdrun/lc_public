#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/contains-duplicate-iii/description/

Given an array of integers,

find out whether there are two distinct indices i and j in the array

such that the absolute difference between nums[i] and nums[j] is *at most* t

and the absolute difference between i and j is *at most* k.

值得差異: 至多 t
index差異: 至多k

1. 找值得差異: current value + t , current value - t
2. index差異: 每一次便刪除前面超過距離的值.
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int idx
        :type t: int value
        :rtype: bool
        """
        from __builtin__ import xrange
        import bisect as bi

        ary = []

        for i in xrange(len(nums)):
            # 定調 value range.
            plus = nums[i] + t
            minus = nums[i] - t

            pidx = bi.bisect_left(ary, plus)

            # 表示沒有且爆表...
            if pidx > len(ary) - 1:
                pidx -= 1

            if len(ary) and ary[pidx] <= plus and ary[pidx] >= nums[i]:
                return True

            midx = bi.bisect_left(ary, minus)

            #  print("midx: {}".format(midx))
            #  print("minus: {}".format(minus))
            #  print("aru: {}".format(ary))
            #  print("\n\n")

            if midx > len(ary) - 1:
                midx -= 1

            if len(ary) and ary[midx] >= minus and ary[midx] <= nums[i]:
                return True

            bi.insort(ary, nums[i])

            # 重要! 確保 ary內為idx k 範圍內的合法value.
            if i >= k:
                ary.remove(nums[i - k])

        return False

    def rewrite(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int idx
        :type t: int value
        :rtype: bool
        """
        from __builtin__ import xrange
        import bisect as bi

def build():
    return [-1, -1], 1, -1
    return [7, 8, 5, 2, 3], 2, 2
    return [1, 3, 2, 4], 2, 1


if __name__ == "__main__":

    s = Solution()
    result = s.containsNearbyAlmostDuplicate(*build())

    print(result)
