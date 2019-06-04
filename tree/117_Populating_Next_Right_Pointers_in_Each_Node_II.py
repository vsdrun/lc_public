#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree?
Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,

         1
       /  \
      2    3
     / \    \
    4   5    7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, node):
        tail = dummy = TreeLinkNode(0)

        while node:
            tail.next = node.left

            if tail.next:
                tail = tail.next

            tail.next = node.right

            if tail.next:
                tail = tail.next

            node = node.next

            if not node:
                tail = dummy  # 重新初始tail..
                node = dummy.next


def build():
    """
         1
       /  \
      2    3
     / \    \
    4   5    7
    """
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    root.right.right = TreeLinkNode(7)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
    return root
    return None

def pp(node):
    root = [node]

    while root:
        r = root[0]
        tmp = []
        while r:
            tmp.append(r.val)
            r = r.next
        print(tmp)

        tmp = []
        for n in root:
            if n.left:
                tmp.append(n.left)
            if n.right:
                tmp.append(n.right)
        root = tmp

if __name__ == "__main__":
    s = Solution()
    tree = build()
    s.connect(tree)
    pp(tree)
