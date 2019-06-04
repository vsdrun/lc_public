#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/merge-k-sorted-lists/description/

Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.
"""

import itertools
import Queue
import random


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(None)
        ln = dummy
        # 類似heap data structure.
        q = Queue.PriorityQueue()

        for l in lists:
            if l:
                q.put((l.val, l))

        while q.qsize():
            ln.next = q.get()[1]
            ln = ln.next
            if ln.next:
                q.put((ln.next.val, ln.next))

        return dummy.next

    def rewrite(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq as hq

        orig = ret = ListNode(None)

        stack = []

        [hq.heappush(stack, (l.val, idx)) for idx, l in enumerate(lists) if l]

        while stack:
            val, idx = hq.heappop(stack)

            ret.next = ListNode(val)
            ret = ret.next

            lists[idx] = lists[idx].next

            if lists[idx]:
                hq.heappush(stack, (lists[idx].val, idx))

        return orig.next


def build():
    c = itertools.count(random.uniform(0, 1000))
    l = ListNode(next(c))
    l_next = l

    for i in range(0):
        l_next.next = ListNode(next(c))
        l_next = l_next.next

    return l


if __name__ == "__main__":

    lists = []

    for i in range(3):
        lists.append(build())

    s = Solution()
    tmp_result = s.mergeKLists(lists)

    while tmp_result:
        print(tmp_result.val)
        tmp_result = tmp_result.next
    print("\n\n")
    # -------------------
    lists = []
    for i in range(3):
        lists.append(build())
    lists = [[]]
    tmp_result = s.rewrite(lists)

    while tmp_result:
        print(tmp_result.val)
        tmp_result = tmp_result.next
