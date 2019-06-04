#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/contiguous-array/description/

Given a binary array,
find the **maximum** length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation:
[0, 1] is the longest contiguous subarray with equal number of 0 and 1.


Example 2:
Input: [0,1,0]
Output: 2
Explanation:
[0, 1] (or [1, 0]) is a longest contiguous
subarray with equal number of 0 and 1.

https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation
"""


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        請思考連續累加圖形.
        """
        count = 0
        max_length = 0

        # 起始為0 重要!!  因為為原點.
        table = {0: 0}

        for index, num in enumerate(nums, 1):  # 起始為 1 重要!!
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index

        return max_length


def build():
    return [0, 1, 1, 1, 0, 0, 1, 1]
    return [0, 1, 0]
    return [0, 1, 1]  # answer: 2
    return [1, 1, 0]  # answer: 2
    return [0, 1]


if __name__ == "__main__":

    s = Solution()
    result = s.findMaxLength(build())

    print(result)
