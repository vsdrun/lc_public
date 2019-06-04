#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/intersection-of-two-linked-lists/description/

Write a program to find the node at which the
intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

smart solution:
https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/126920/Python-code-with-clear-explanation
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        pa = headA
        pb = headB

        """
        if the two linked lists have intersection,
        and if you go through A + B vs B + A,
        you should see the intersection node at some point
        e.g. A: a1, a2, c1, c2, c3, B: b1, b2, b3, c1, c2, c3
        A -> B (link B to the end of A): a1, a2, c1, c2, c3, b1, b2, b3, c1, c2, c3
        B -> A (link A to the end of B): b1, b2, b3, c1, c2, c3, a1, a2, c1, c2, c3
        As you can see, the intersection is at c1 (the third element from the tail)
        If there's no intersection, the loop will exit because both pointer is None
        """

        while pa != pb:
            # None == None while hits the end , thus exist while loop.
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA

        return pa if pa else None


def build():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    l6 = ListNode(6)
    l7 = ListNode(7)
    l6.next = l7
    #  l7.next = l3

    return l1, l6


if __name__ == "__main__":
    s = Solution()
    print(s.getIntersectionNode(*build()))
