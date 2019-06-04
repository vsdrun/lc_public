#!/usr/bin/env python


"""
https://leetcode.com/problems/merge-two-sorted-lists/description/

Merge two sorted linked lists and return it as a new list.

The new list should be made by splicing together
the nodes of the first two lists.


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

        import heapq

        def show(lst):
            while lst:
                yield lst.val
                lst = lst.next

        b = map(show, (l1, l2))
        m = heapq.merge(*b)

        result = []

        for i in m:
            result.append(i)

        return result


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
    l8 = ListNode(8)
    l9 = ListNode(9)
    l6.next = l7
    l7.next = l8
    l8.next = l9
    return l1, l6


if __name__ == "__main__":
    s = Solution()
    print(s.mergeTwoLists(*build()))
