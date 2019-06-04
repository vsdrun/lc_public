#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/add-two-numbers-ii/description/

You are given two non-empty linked lists representing two non-negative
integers.

The most significant digit comes first and each of their
nodes contain a single digit.
Add the two numbers and return it as a linked list.


You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Follow up:
What if you cannot modify the input lists?
In other words, reversing the lists is not allowed.

這時就要想, 怎麼reverse?
用stack!

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""


def pp(node):
    while node:
        print(node.val)
        node = node.next


# Definition for singly-linked list.


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
        l1_stack = []
        l2_stack = []

        while l1:
            l1_stack.append(l1.val)
            l1 = l1.next

        while l2:
            l2_stack.append(l2.val)
            l2 = l2.next

        carry = 0
        pre_head = None
        head = None

        while l1_stack and l2_stack:
            v1 = l1_stack.pop()
            v2 = l2_stack.pop()
            ssum = v1 + v2 + carry
            carry = 0
            digit = ssum % 10
            carry = ssum / 10
            head = ListNode(digit)
            head.next = pre_head
            pre_head = head

        while l1_stack:
            v1 = l1_stack.pop()
            ssum = v1 + carry
            carry = 0
            digit = ssum % 10
            carry = ssum / 10
            head = ListNode(digit)
            head.next = pre_head
            pre_head = head

        while l2_stack:
            v2 = l2_stack.pop()
            ssum = v2 + carry
            carry = 0
            digit = ssum % 10
            carry = ssum / 10
            head = ListNode(digit)
            head.next = pre_head
            pre_head = head

        if carry:
            head = ListNode(carry)
            head.next = pre_head

        return head

    def rewrite(self, l1, l2):
        """
        Use extra stack space to add result.
        """
        l1Stack = []
        l2Stack = []

        def fill(stack, li):
            while li:
                stack.append(li.val)
                li = li.next

        fill(l1Stack, l1)
        fill(l2Stack, l2)

        prev = None

        while l1Stack and l2Stack:
            if prev:
                cv = prev.val + l1Stack.pop() + l2Stack.pop()
                prev.val = cv % 10
                tmp = ListNode(cv / 10)
                tmp.next = prev
                prev = tmp
            else:
                cv = l1Stack.pop() + l2Stack.pop()
                tmp = ListNode(cv % 10)
                prev = ListNode(cv / 10)
                prev.next = tmp

        def single(stack, prev):
            while stack:
                if prev:
                    cv = prev.val + stack.pop()
                    prev.val = cv % 10
                    tmp = ListNode(cv / 10)
                    tmp.next = prev
                    prev = tmp
                else:
                    tmp = ListNode(stack.pop())
                    prev = ListNode(None)
                    prev.next = tmp
            return prev

        prev = single(l1Stack, prev)
        prev = single(l2Stack, prev)

        return prev if prev.val else prev.next


def build():
    """
    (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    [1] + [9,9]
    """
    n1 = ListNode(1)
    n9 = ListNode(9)
    n99 = ListNode(9)
    n9.next = n99
    return n1, n9

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

    result = s.rewrite(l1, l2)
    pp(result)
