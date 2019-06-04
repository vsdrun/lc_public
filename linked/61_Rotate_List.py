#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/rotate-list/description/

Given a linked list,
rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode

        這個太慢啦!!!
        """
        from __builtin__ import xrange
        if not head:
            return

        def move(node):
            onode = node
            prev = None
            ppnode = None

            while node:
                ppnode = prev
                prev = node
                node = node.next

            prev.next = onode

            if ppnode:
                ppnode.next = None
            else:
                prev.next = None

            return prev

        for _ in xrange(k):
            head = move(head)

        return head

    def rewrite(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        from __builtin__ import xrange

        if not head:
            return

        # 先算長度...
        cnt = 0
        ohead = head

        while head:
            cnt += 1
            head = head.next

        k %= cnt
        head = ohead


        def move(node):
            onode = node
            prev = None
            ppnode = None

            while node:
                ppnode = prev
                prev = node
                node = node.next

            prev.next = onode

            if ppnode:
                ppnode.next = None
            else:
                prev.next = None
            return prev

        for _ in xrange(k):
            head = move(head)

        return head

def build():
    #  Input: 1->2->3->4->5->NULL, m = 2, n = 4
    #  Output: 1->4->3->2->5->NULL
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    #  head.next.next.next = ListNode(4)
    #  head.next.next.next.next = ListNode(5)
    #  head.next.next.next.next.next = ListNode(6)
    #  head.next.next.next.next.next.next = ListNode(7)
    return head, 200000000

def pp(node):
    result = []

    while node:
        result.append(node.val)
        node = node.next
    print(result)

if __name__ == "__main__":
    s = Solution()
    pp(build()[0])
    pp(s.rewrite(*build()))
