#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/kth-largest-element-in-an-array/description/

Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order,
not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

***
PYTHON:
Queue.PriorityQueue is a thread-safe class, while the heapq module makes no
thread-safety guarantees.
"""

import random
import Queue


class Solution(object):

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = Queue.PriorityQueue()

        for n in nums:
            if q.qsize() == (k + 1):
                q.get()
            q.put(n)

        while q.qsize() != k:
            q.get()

        return q.get()

    def rewrite(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq

        ary = []

        for i in nums:
            heapq.heappush(ary, i)

            if len(ary) > k:
                heapq.heappop(ary)

        return heapq.heappop(ary)


def build():
    return [random.randrange(0, 1000) for _ in xrange(12)], 3


if __name__ == "__main__":
    s = Solution()
    b = build()
    print(b[0])
    result = s.findKthLargest(*b)
    print(result)
    result = s.rewrite(*b)
    print(result)
