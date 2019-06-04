#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/copy-list-with-random-pointer/description/

A linked list is given such that each node contains an additional
random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return

        orig_head = head

        while head:
            cln = RandomListNode(head.label)
            cln.random = head.random
            cln.next = head.next
            cln.FUCK = cln.label
            head.next = cln
            head = cln.next

        clone_head = orig_head.next
        head = orig_head

        # assign clone nodes' random
        while head:
            head = head.next
            head.random = head.random.next if head.random else None
            head = head.next

        head = orig_head

        # detach
        while head:
            o_head = head
            o_next = head.next.next if head.next else None

            head = head.next
            head.next = head.next.next if head.next else None

            o_head.next = o_next
            head = o_next

        return clone_head

    def rewrite(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode

        class RandomListNode(object):
            def __init__(self, x):
                self.label = x
                self.next = None
                self.random = None
        """
        ohead = head

        while head:
            newHead = RandomListNode(head.label)
            newHead.random = head.random
            nh = head.next
            head.next = newHead
            newHead.next = nh
            head = nh

        head = ohead
        while head:
            newHead = head.next
            newHead.random = newHead.random.next if newHead.random else None
            head = newHead.next

        # detach newHead
        rnewHead = None
        head = ohead

        while head:
            if not rnewHead:
                rnewHead = head.next

            newHead = head.next
            nh = newHead.next
            head.next = nh
            head = nh
            newHead.next = head.next if head else None

        return rnewHead

    def rewrite2(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode

        class Node(object):
            def __init__(self, val, next, random):
                self.val = val
                self.next = next
                self.random = random
        """
        ohead = head
        # create head->newhead->n2->newN2->None
        while head:
            newHead = Node(head.val, head.next, head.random)
            head.next = newHead
            head = newHead.next

        head = ohead
        nhead = head.next
        # assign newHead.random and detach
        while head:
            newHead = head.next
            newHead.random = newHead.random.next
            head.next = newHead.next
            newHead.next = newHead.next.next if newHead.next else None
            head = head.next

        return nhead

def build():
    head = RandomListNode(3)
    a = RandomListNode(4)
    e = RandomListNode(4)
    b = RandomListNode(5)
    c = RandomListNode(6)
    d = RandomListNode(7)

    head.next = a
    a.next = e
    e.next = b
    b.next = c
    c.next = d
    head.random = d
    a.random = b
    b.random = c
    c.random = a
    d.random = c
    e.random = d
    return head

def build2():
    head = Node(3, None, None)
    a = Node(4, None, None)
    e = Node(4, None, None)
    b = Node(5, None, None)
    c = Node(6, None, None)
    d = Node(7, None, None)

    head.next = a
    a.next = e
    e.next = b
    b.next = c
    c.next = d
    head.random = d
    a.random = b
    b.random = c
    c.random = a
    d.random = c
    e.random = d
    return head

if __name__ == "__main__":
    s = Solution()
    result = s.copyRandomList(build())
    while result:
        print(result.label)
        result = result.next

    print("----")
    result = s.rewrite(build())

    while result:
        print(result.label)
        result = result.next

    print("----")
    result = s.rewrite2(build2())

    while result:
        print(result.val)
        result = result.next
