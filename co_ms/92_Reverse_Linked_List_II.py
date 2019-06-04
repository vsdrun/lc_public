#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/reverse-linked-list-ii/description/

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        cnt = 0
        ohead = head
        prev = None

        def reverse(node, cnt):
            prev = None
            lcnt = 0
            this_node = node

            while node and lcnt < cnt:
                nnext = node.next
                node.next = prev
                prev = node
                node = nnext
                lcnt += 1

            this_node.next = node

            return prev

        while head:
            cnt += 1

            if cnt == m:
                result= reverse(head, n - m + 1)
                if prev:
                    prev.next = result
                else:
                    ohead = result
                break
            else:
                prev = head
                head = head.next

        return ohead

def build():
    #  Input: 1->2->3->4->5->NULL, m = 2, n = 4
    #  Output: 1->4->3->2->5->NULL
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    return head, 5, 8

def pp(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

if __name__ == "__main__":
    s = Solution()
    pp(build()[0])
    pp(s.reverseBetween(*build()))
