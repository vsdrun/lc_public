#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/add-two-numbers/description/


You are given two non-empty linked lists representing two
non-negative integers.

The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        ret_head = head = ListNode(float("-inf"))

        while l1 and l2:
            summ = l1.val + l2.val + carry
            l1 = l1.next
            l2 = l2.next
            digit = summ % 10
            carry = summ / 10
            current_node = ListNode(digit)
            head.next = current_node
            head = current_node

        while l1:
            summ = l1.val + carry
            l1 = l1.next
            digit = summ % 10
            carry = summ / 10
            current_node = ListNode(digit)
            head.next = current_node
            head = current_node

        while l2:
            summ = l2.val + carry
            l2 = l2.next
            digit = summ % 10
            carry = summ / 10
            current_node = ListNode(digit)
            head.next = current_node
            head = current_node

        if carry:
            current_node = ListNode(carry)
            head.next = current_node
            head = current_node

        return ret_head.next


def build():
    """
    (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    """

    n7 = ListNode(7)
    n2 = ListNode(2)
    n4 = ListNode(4)
    n3 = ListNode(3)
    n7.next = n2
    n2.next = n4
    n4.next = n3

    n5 = ListNode(5)
    n6 = ListNode(6)
    n4 = ListNode(4)

    n5.next = n6
    n6.next = n4

    return n7, n5


if __name__ == "__main__":
    l1, l2 = build()

    s = Solution()
    result = s.addTwoNumbers(l1, l2)

    pp(result)
