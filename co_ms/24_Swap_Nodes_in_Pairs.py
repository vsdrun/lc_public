#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/swap-nodes-in-pairs/description/


Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes,
only nodes itself may be changed.
"""


def pp(node):
    while node:
        print(node.val)
        node = node.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret_head = head.next if head and head.next else head

        pp_head = None

        while head:
            if not head.next:
                break

            pre_head = head
            cur_head = head.next
            next_head = cur_head.next

            cur_head.next = pre_head
            pre_head.next = next_head

            if pp_head:
                pp_head.next = cur_head

            pp_head = pre_head

            head = next_head

        return ret_head

    def rewrite(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret_head = head.next if head and head.next else head

        pp_head = None

        while head:
            if not head.next:
                break

            pre_head = head
            cur_head = head.next
            next_head = cur_head.next

            cur_head.next = pre_head
            pre_head.next = next_head

            if pp_head:
                pp_head.next = cur_head

            pp_head = pre_head

            head = next_head

        return ret_head


def build():
    """
    (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    """

    n7 = ListNode(7)
    n2 = ListNode(2)
    n4 = ListNode(4)
    n3 = ListNode(3)
    n5 = ListNode(5)
    n7.next = n2
    n2.next = n4
    n4.next = n3
    n3.next = n5

    return n7


if __name__ == "__main__":
    l1 = build()

    s = Solution()
    result = s.swapPairs(l1)

    pp(result)
