#!/usr/bin/env python


"""
https://leetcode.com/problems/delete-node-in-a-linked-list/description/

Write a function to delete a node (except the tail)
in a singly linked list,
given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4
and you are given the third node with value 3,
the linked list should become 1 -> 2 -> 4 after calling your function.
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


def build():
    return


if __name__ == "__main__":
    s = Solution()
    s.deleteNode(build())
