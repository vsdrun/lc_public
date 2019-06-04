#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/smallest-range/description/

You have k lists of sorted integers in ascending order.

Find the smallest range that includes at least one number from
each of the k lists.

We define the range [a,b] is smaller than range
[c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]

Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
"""


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        1. 先 sort
        2. 由頭往後找 涵蓋所有 k list後 由前往後減少.
        以上慢...
        可否~
        直接從 heap sort中找到最小區間?
        可以！
        """

        import heapq as hq

        # (first value, which list, each row's moving index)
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        hq.heapify(heap)

        final_right, final_left = float("inf"), float("-inf")

        right = max(t[0] for t in heap)

        while heap:
            # pop the smallest
            value, which_row, row_idx = hq.heappop(heap)

            left = value

            if right - left < final_right - final_left:
                final_right, final_left = right, left

            # 注意! 當任一 row 走到底時 end loop!
            row_idx += 1

            if row_idx == len(nums[which_row]):
                return [final_left, final_right]

            # update right for next loop.
            right = max(right, nums[which_row][row_idx])

            hq.heappush(heap, (nums[which_row][row_idx], which_row, row_idx))


def build():
    return [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]


if __name__ == "__main__":
    s = Solution()
    print(s.smallestRange(build()))
