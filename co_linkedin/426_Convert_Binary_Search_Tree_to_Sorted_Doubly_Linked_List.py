#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

Convert a BST to a sorted circular doubly-linked list in-place.
Think of the left and right pointers as synonymous to the previous
and next pointers in a doubly-linked list.

Let's take the following BST as an example,
it may help you understand the problem better:

fig_1



We want to transform this BST into a circular doubly linked list.
Each node in a doubly linked list has a predecessor and successor.
For a circular doubly linked list,
the predecessor of the first element is the last element,
and the successor of the last element is the first element.

The figure below shows the circular doubly linked list for the BST above.
The "head" symbol means the node it points to is the smallest element of
the linked list.

fig_2



Specifically, we want to do the transformation in place.
After the transformation,
the left pointer of the tree node should point to its predecessor,
and the right pointer should point to its successor.
We should return the pointer to the first element of the linked list.


The figure below shows the transformed BST.
The solid line indicates the successor relationship,
while the dashed line means the predecessor relationship.

fig_3

"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return

        def traverse(node):
            """
            ret: node's min, max
            左 assign 左邊的largest, 右 assign 右邊的smallest
            """
            lmin = lmax = rmin = rmax = None

            if node.left:
                lmin, lmax = traverse(node.left)

            if node.right:
                rmin, rmax = traverse(node.right)

            node.right = rmin
            node.left = lmax

            if not rmax:
                rmax = node

            if not lmin:
                lmin = node

            if lmax:
                lmax.right = node
            if rmin:
                rmin.left = node

            return lmin, rmax



        mmin, mmax = traverse(root)

        mmin.left = mmax
        mmax.right = mmin

        return mmin

    def rewrite(self, root):
        """
        :type root: Node
        :rtype: Node
        SMART.
        """

        stack = []

        while root:
            stack.append(root)
            root = root.left

        prev = head = Node(None, None, None)

        while stack:
            cur = stack.pop()
            prev.right = cur
            cur.left= prev
            prev = cur

            if cur.right:
                root = cur.right
                while root:
                    stack.append(root)
                    root = root.left

        head.right.left = prev
        prev.right = head.right

        return head.right

    def rewrite4(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # use stack to the rescue
        if not root:
            return

        dummy = prev = Node(None, None, None)
        stack = []

        while root:
            stack.append(root)
            root = root.left

        while stack:
            curr = stack.pop()
            prev.right = curr
            curr.left = prev
            prev = curr

            tnode = curr.right
            while tnode:
                stack.append(tnode)
                tnode = tnode.left

        prev.right = dummy.right
        dummy.right.left = prev

        return dummy.right


def build():
    n1 = Node(1, None, None)
    n3 = Node(3, None, None)
    n5 = Node(5, None, None)
    n2 = Node(2, n1, n3)
    n4 = Node(4, n2, n5)
    return n4


def pp(node, reverse=False):
    result = []
    headnode = node

    while node:
        result.append(node.val)
        node = node.right if not reverse else node.left
        if node == headnode:
            break

    print(result)


if __name__ == "__main__":
    s = Solution()
    r = s.treeToDoublyList(build())
    pp(r)
    pp(r, True)

    print("---")
    r = s.rewrite(build())
    pp(r)
    pp(r, True)
