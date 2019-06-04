#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/sliding-window-maximum/description/


Given an array nums, there is a sliding window of size k which is
moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""
import collections


class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        """
        想法:
        k 個裡面只留最大值的index.
        若最大值的index跳出sliding window範圍，pop掉.
        """
        result = []

        if len(nums) == 0:
            return result

        # 用deque來存nums的index, fast left pop, right pop.
        d_heap = collections.deque()

        for i, v in enumerate(nums):
            # it's a while loop. Making the deque as Max heap.
            # 很重要!
            # 如果是(3,2,1) 則保留2,1供下一個set使用
            # 如果是(1,3,2) 則清掉1 留3,2
            # 如果是(1,2,3) 則清掉1,2 留3.
            while d_heap and nums[d_heap[-1]] < v:  # 2. 若新加的值大於前一個
                                                    # 則將前一個給pop掉
                print("current input v: {0}".format(v))
                d_heap.pop()  # 確保清掉小的

            d_heap += i,  # 1.

            if d_heap[0] == (i - k):  # 3. sliding window, 將左pop
                d_heap.popleft()

            # 確保 i 目前已經超過或者等於k個.
            if i >= (k - 1):
                result += nums[d_heap[0]],

        return result


def build_list():
    l = [2, 1, 3]
    l = [1, 3, 1, 2, 0, 5]

    return l


if __name__ == "__main__":
    input_list = build_list()
    print("input: {0}".format(input_list))
    s = Solution()
    result = s.maxSlidingWindow(input_list, 3)
    # expect: [3,3,2,5]
    print(result)
