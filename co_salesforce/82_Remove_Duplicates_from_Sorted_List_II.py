#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

Given a sorted linked list,
delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

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
        ret = tmp = ListNode(None)
        tmp.next = head

        while head:
            dup = False

            while head.next and head.val == head.next.val:
                head.next = head.next.next
                dup = True

            if dup:
                tmp.next = head.next
                head = tmp.next
            else:
                head = head.next
                tmp = tmp.next

        return ret.next



def build():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(5)
    return head
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    return head

def pp(node):
    tmp = []

    while node:
        tmp.append(node.val)
        node = node.next

    print(tmp)

if __name__ == "__main__":

    s = Solution()
    pp(s.deleteDuplicates(build()))
