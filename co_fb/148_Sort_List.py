#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/sort-list/


Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        merge sort
        """

        def get_two(node):
            """
            :node: node, should not be None
            :ret: 2 lists cut from the middle
            """
            head = node
            prev = head
            nxt = head.next if head else None

            while nxt:
                prev = head
                head = head.next
                nxt = nxt.next

            prev.next = None
            return node, head if node != head else None


        def merge(nodes):
            """
            split nodes
            return merges result
            """
            if not nodes:
                return

            h1, h2 = get_two(nodes)

            if h2 is None:
                # nodes is single node
                return h1

            #  print("h1: {}".format(h1.val))
            #  print("h2: {}".format(h2.val))
            m1 = merge(h1)
            m2 = merge(h2)
            #  print("m1: {}".format(m1.val))
            #  print("m1.next: {}".format(m1.next))
            #  print("m2: {}".format(m2.val))
            #  print("m2.next: {}".format(m2.next))

            ret = tmp = ListNode(None)

            while m1 and m2:
                if m1.val >= m2.val:
                    tmp.next = m2
                    tmp = tmp.next
                    m2 = m2.next
                else:
                    tmp.next = m1
                    tmp = tmp.next
                    m1 = m1.next

            if m1:
                #  print("shit1")
                #  print("tmp: {}".format(tmp.val))
                tmp.next = m1
            if m2:
                #  print("shit2")
                #  print("tmp: {}".format(tmp.val))
                tmp.next = m2

            #  print("ret: {}".format(ret.val))
            #  print("ret.next: {}".format(ret.next.val))
            return ret.next


        return merge(head)

def build():
#  Input: -1->5->3->4->0
    _1 = ListNode(-1)
    _5 = ListNode(5)
    _3 = ListNode(3)
    _4 = ListNode(4)
    _0 = ListNode(0)

    _1.next = _0
    return _1
    # -------------
    #  _5.next = _1
    #  return _5
    # -------------
    _1.next = _5
    _5.next = _3
    _3.next = _4
    _4.next = _0
    return _1


def pp(nodes):
    result = []

    while nodes:
        result.append(nodes.val)
        nodes = nodes.next

    print(result)

if __name__ == "__main__":
    s = Solution()
    ret = s.sortList(build())
    pp(ret)
