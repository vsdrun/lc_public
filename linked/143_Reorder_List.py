#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/reorder-list/description/

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.

        觀察:
        先取前面一半的list. 後面一半reverse.
        依序插入~~~
        """
        if not head:
            return

        def getHalf(node):
            slow = node
            fast = node.next.next if node.next else None

            while fast:
                fast = fast.next.next if fast.next else None
                slow = slow.next

            nhalf = slow.next
            slow.next = None

            return nhalf

        def reverse(node):
            prev = None

            while node:
                nnode = node.next
                node.next = prev
                prev = node
                node = nnode

            return prev

        nhalf = getHalf(head)
        nhalf = reverse(nhalf)

        new_head = head

        while new_head:
            nnode = new_head.next
            new_head.next = nhalf
            nhalf = nhalf.next if nhalf else None
            if new_head.next:
                new_head.next.next = nnode
            new_head = nnode




def build():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    return head


if __name__ == "__main__":
    s = Solution()
    r = s.reorderList(build())

    result = []
    while r:
        result.append(r.val)
        r = r.next

    print(result)
    
