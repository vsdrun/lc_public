#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/odd-even-linked-list/description/

Given a singly linked list, group all odd nodes together followed by the
even nodes.

Please note here we are talking about the node number
and not the value in the nodes.

You should try to do it in place.
The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
"""

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        def change(node):
            """
            modify odd/even node's next
            """
            theeven = peven = None
            lastodd = None

            while node:
                even= node.next if node else None

                if peven:
                    peven.next = even

                if not theeven:
                    theeven = even

                peven = even

                node.next = node.next.next if node.next else None
                lastodd = node
                node = node.next
            lastodd.next = theeven
        change(head)
        return head

def build():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    return head


if __name__ == "__main__":
    s = Solution()
    r = s.oddEvenList(build())

    result = []
    while r:
        result.append(r.val)
        r = r.next

    print(result)
    
