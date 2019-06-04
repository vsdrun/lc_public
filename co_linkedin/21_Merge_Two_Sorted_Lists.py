#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/merge-two-sorted-lists/description/

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing
together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = head = ListNode(None)

        while l1 and l2:
            if l1.val <= l2. val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next

            dummy = dummy.next

        if l1:
            dummy.next = l1
        else:
            dummy.next = l2

        return head.next


def build():
    l1 = ListNode(1)
    l1.next = ListNode(5)
    l1.next.next = ListNode(8)

    l2 = ListNode(1)
    l2.next = ListNode(7)
    l2.next.next = ListNode(9)

    return l1, l2


if __name__ == "__main__":
    s = Solution()
    r = s.mergeTwoLists(*build())

    while r:
        print(r.val)
        r = r.next
