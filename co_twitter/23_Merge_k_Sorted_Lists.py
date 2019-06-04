#!/usr/bin/env python


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


def build():
    c = itertools.count(random.uniform(0, 1000))
    l = ListNode(next(c))
    l_next = l

    for i in xrange(0):
        l_next.next = ListNode(next(c))
        l_next = l_next.next

    return l


if __name__ == "__main__":

    lists = []

    for i in xrange(30000):
        lists.append(build())

    s = Solution()
    tmp_result = s.mergeKLists(lists)

    while tmp_result:
        print(tmp_result.val)
        tmp_result = tmp_result.next
