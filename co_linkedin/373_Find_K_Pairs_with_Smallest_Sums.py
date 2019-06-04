#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/


"""
You are given two integer arrays nums1 and nums2 sorted
in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first
array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.


Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3
Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]


Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]


Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]


https://discuss.leetcode.com/topic/50450/slow-1-liner-to-fast-solutions/2

def kSmallestPairs(self, nums1, nums2, k):
    queue = []

    def push(i, j):
        if i < len(nums1) and j < len(nums2):
            heapq.heappush(queue, [nums1[i] + nums2[j], i, j])

    push(0, 0)
    pairs = []

    while queue and len(pairs) < k:
        _, i, j = heapq.heappop(queue)
        pairs.append([nums1[i], nums2[j]])
        push(i, j + 1)
        if j == 0:
            push(i + 1, 0)

    return pairs
"""

import heapq


class Solution(object):

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        這是比較慢的解決方案。
        較好的是想成matrix.
        需要時一個row一個row的加入
        """
        if not nums1 or not nums2:
            return []

        h_list = []

        for n1 in nums1:
            for n2 in nums2:
                heapq.heappush(h_list, (n1 + n2, n1, n2))

        result = []

        for i in xrange(k):
            try:
                _, n1, n2 = heapq.heappop(h_list)
            except Exception:
                break
            result += [n1, n2],

        return result

    def rewrite(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        BEST solution
        """
        tmp = []

        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(tmp, [nums1[i] + nums2[j], i, j])

        push(0, 0)
        result = []

        while tmp and len(result) < k:
            print("tmp: {}".format(tmp))
            _, i, j = heapq.heappop(tmp)
            print("pop tmp: {}".format(tmp))
            result.append([nums1[i], nums2[j]])
            push(i, j + 1)
            # 重要!!!
            if j == 0:
                push(i + 1, 0)

        return result


def build():
    l1 = [1, 1, 2]
    l2 = [1, 2, 3]
    l1 = [1,1,2]
    l2 = [1,2,3]
    l1 = [1,2,3,3,3]
    l2 = [-3,22,35,56,70,100,123,200]
    return l1, l2, 10


if __name__ == "__main__":
    s = Solution()
    print(s.kSmallestPairs(*build()))
    print(s.rewrite(*build()))
