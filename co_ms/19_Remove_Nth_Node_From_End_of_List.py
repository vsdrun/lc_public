#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/


Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        orig = forward = head
        cnt = 0  # 比 n 多 1 才行 要在移除的node之前 才能modify list...

        while forward.next and cnt < n:
            forward = forward.next
            cnt += 1

        if cnt == (n - 1):
            orig = orig.next
        elif cnt < n:
            return orig
        else:
            while forward.next:
                head = head.next
                forward = forward.next

            head.next = head.next.next

        return orig

    def rewrite(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        ohead = head

        def forward(node, length):
            l = length

            while l > 0 and node:
                node = node.next
                l -= 1

            return node, l

        sNode, l = forward(head, n)

        if not sNode:
            if l > 0:
                return ohead
            else:
                # 注意此... 1->None, 1 的情況.
                head = head.next
                ohead.next = None
                return head

        while sNode.next:
            head = head.next
            sNode = sNode.next

        oNext = head.next
        head.next = oNext.next
        oNext.next = None
        return ohead


def build():
    node = ListNode(1)
    return node, 1
    #  Given linked list: 1->2->3->4->5, and n = 2.
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)

    return node, 3


def pp(node):
    result = []

    while node:
        result.append(node.val)
        node = node.next
    print(result)


if __name__ == "__main__":
    s = Solution()
    pp(s.removeNthFromEnd(*build()))
    pp(s.rewrite(*build()))
