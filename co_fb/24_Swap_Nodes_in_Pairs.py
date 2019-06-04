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
        Fast solution, but hard to fathom.
        """
        pre = ListNode(-1)
        pre.next = head
        curr = pre

        while curr.next and curr.next.next:
            forward = curr.next  # current node

            curr.next = forward.next
            forward.next = forward.next.next  # next loop head
            curr.next.next = forward

            curr = forward

        return pre.next

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

    def rewrite2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Given 1->2->3->4, you should return the list as 2->1->4->3.
        """
        nextloop = None
        rethead = None

        while head:
            # do one thing, swap, make the end node for next loop
            current_head = head
            nh = current_head.next if current_head else None

            if not rethead:
                if nh:
                    rethead = nh
                else:
                    rethead = current_head

            head = nh.next if nh else None

            if nh:
                nh.next = current_head

            if nextloop:
                nextloop.next = nh if nh else current_head

            nextloop = current_head

        if nextloop:
            nextloop.next = None

        return rethead

    def rewrite3(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Given 1->2->3->4, you should return the list as 2->1->4->3.

        haha, use stack of size 2
        """
        stack = []

        ptail = None
        retHead = None

        while head:
            tmp = head.next

            if len(stack) == 1:
                if ptail:
                    ptail.next = head

                pnode = stack.pop()
                pnode.next = None

                head.next = pnode
                ptail = pnode

                if not retHead:
                    retHead = head


            else:
                stack.append(head)

            head = tmp

        if stack:
            pnode = stack.pop()

            if not retHead:
                retHead = pnode

            if ptail:
                ptail.next = pnode

        return retHead

def build():
    """
    (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    """
    n7 = ListNode(7)
    n2 = ListNode(2)
    n4 = ListNode(4)
    n3 = ListNode(3)
    #  n5 = ListNode(5)
    n7.next = n2
    n2.next = n4
    return n7
    n4.next = n3
    #  n3.next = n5


if __name__ == "__main__":
    s = Solution()
    pp(s.swapPairs(build()))
    print("--")
    pp(s.rewrite(build()))
    print("--")
    pp(s.rewrite2(build()))
    print("--")
    pp(s.rewrite3(build()))
