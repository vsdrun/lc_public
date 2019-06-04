#!/usr/bin/env python


"""
https://leetcode.com/problems/reverse-linked-list/description/

Reverse a singly linked list.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None

        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur

        return prev

    def rewrite(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None

        while head:
            nh = head.next
            head.next = prev
            prev = head
            head = nh

        return prev


def build():
    import itertools
    import random
    c = itertools.count(int(random.uniform(0, 1000)))

    ll = ListNode(next(c))
    l_next = ll

    for i in xrange(5):
        l_next.next = ListNode(next(c))
        l_next = l_next.next

    return ll


if __name__ == "__main__":

    def pp(ll, prt_str):
        if not ll:
            print(prt_str)
            return

        if prt_str:
            prt_str += "->"

        prt_str += str(ll.val)
        pp(ll.next, prt_str)

    s = Solution()
    ll = build()
    pp(ll, "")
    #  lr = s.reverseList(ll)
    #  pp(lr, "")
    lr = s.rewrite(ll)
    pp(lr, "")
