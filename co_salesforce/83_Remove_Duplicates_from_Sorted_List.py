#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

Given a sorted linked list,
delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head

        while head:
            if head.next:
                if head.val == head.next.val:
                    head.next = head.next.next
                    continue
            head = head.next

        return tmp

    def rewrite(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ohead = head

        while head:
            if head.next and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return ohead


def build():
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(5)
    return head


def pp(node):
    print(node.val)
    tmp = []

    while node:
        tmp.append(node.val)
        print("node val: {}".format(node.val))
        node = node.next

    print(tmp)


if __name__ == "__main__":

    s = Solution()
    pp(s.deleteDuplicates(build()))
    print("---")
    pp(s.rewrite(build()))
