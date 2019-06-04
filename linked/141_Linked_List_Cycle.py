#!/usr/bin/env python


"""
https://leetcode.com/problems/linked-list-cycle/description/

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return False

        first = head
        second = head.next.next if head.next else None

        if not second:
            return False

        while first != second:
            first = first.next
            second = second.next.next if second.next else None

            if not second:
                return False
        return True

    def rewrite(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False


        first = head
        second = head.next.next if head.next else None

        if not second:
            return False

        while first != second:
            first = first.next

            second = first.next.next if first.next else None

            if not second:
                return False

        return True



def build():
    l1 = ListNode(1)
    return l1
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    return l1


if __name__ == "__main__":
    s = Solution()
    print(s.hasCycle(build()))
    print(s.rewrite(build()))
