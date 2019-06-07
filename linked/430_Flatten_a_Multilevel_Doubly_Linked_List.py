#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

You are given a doubly linked list which in addition to the next and
previous pointers, it could have a child pointer,
which may or may not point to a separate doubly linked list.


These child lists may have one or more children of their own, and so on,
to produce a multilevel data structure,
as shown in the example below.


Flatten the list so that all the nodes appear in a single-level,
doubly linked list.


You are given the head of the first level of the list.
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        思考 每一個recursive call要做的是什麼
        """
        def flatit(node):
            """
            :ret: last right node
            """
            prev = None

            while node:
                origNext = node.next
                # 重要~
                prev = node

                if node.child:
                    node.next = node.child
                    node.child.prev = node
                    lastNode = flatit(node.child)
                    lastNode.next = origNext

                    if origNext:
                        origNext.prev = lastNode
                    # 重要~
                    prev = lastNode

                node.child = None
                node = origNext

            return prev

        flatit(head)
        return head


def build():
    """
    Input:
    1---2---3---4---5---6--NULL
            |
            7---8---9---10--NULL
                |
                11--12--NULL

    Output:
    1-2-3-7-8-11-12-9-10-4-5-6-NULL
    """
    n1 = Node(1, None, None, None)
    n2 = Node(2, None, None, None)
    n3 = Node(3, None, None, None)
    n4 = Node(4, None, None, None)
    n5 = Node(5, None, None, None)
    n6 = Node(6, None, None, None)
    n7 = Node(7, None, None, None)
    n8 = Node(8, None, None, None)
    n9 = Node(9, None, None, None)
    n10 = Node(10, None, None, None)
    n11 = Node(11, None, None, None)
    n12 = Node(12, None, None, None)

    #  n1.child = n2
    #  n2.child = n3
    #  n3.child = n4

    #  return n1

    # --------------
    n1.next = n2
    n2.prev = n1
    n2.next = n3
    n3.prev = n2  # child
    n3.next = n4
    n4.prev = n3
    n4.next = n5
    n5.prev = n4
    n5.next = n6
    n6.prev = n5
    n7.next = n8
    n8.prev = n7
    n8.next = n9
    n9.prev = n8
    n9.next = n10
    n10.prev = n9
    n11.next = n12
    n12.prev = n11

    n3.child = n7
    n8.child = n11

    return n1

def pp(node):
    result = []
    result2 = []
    prev = None

    while node:
        if node.child:
            print("node should have NO child.")
        result.append(node.val)
        prev = node
        node = node.next

    while prev:
        result2.append(prev.val)
        prev = prev.prev

    print(result)
    print(result2)


if __name__ == "__main__":
    s = Solution()
    r = s.flatten(build())
    pp(r)
