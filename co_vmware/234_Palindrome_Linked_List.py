#!/usr/bin/env python


"""
https://leetcode.com/problems/palindrome-linked-list/description/

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = head
        fast = head
        lnode = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse(node):
            pnode = None

            while node:
                nnode = node.next
                node.next = pnode
                pnode = node
                node = nnode

            return pnode

        rnode = reverse(slow)

        while rnode and lnode:
            if rnode.val != lnode.val:
                return False
            rnode = rnode.next
            lnode = lnode.next

        return True


def build():
    li = ListNode(1)
    li.next = ListNode(2)
    return li
    li.next.next = ListNode(3)
    li.next.next.next = ListNode(2)
    li.next.next.next.next = ListNode(1)
    return li


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(build()))
