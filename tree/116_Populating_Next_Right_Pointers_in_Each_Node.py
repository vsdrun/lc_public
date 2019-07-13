#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/


Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}

Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine,
implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree
(ie, all leaves are at the same level, and every parent has two children).

Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
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
    def connect(self, root):
        tmp_node = rnode = TreeLinkNode(-42)

        while root:
            tmp_node.next = root.left

            if tmp_node.next:
                tmp_node = tmp_node.next

            tmp_node.next = root.right

            if tmp_node.next:
                tmp_node = tmp_node.next

            root = root.next

            if not root:
                tmp_node = rnode
                root = rnode.next

    def rewrite(self, root):
        """
        BFS concept
        """
        if not root:
            return

        tree = [root]

        while tree:
            tmp = []

            for idx in range(1, len(tree)):
                tree[idx - 1].next = tree[idx]

                if tree[idx - 1].left:
                    tmp.append(tree[idx - 1].left)
                if tree[idx - 1].right:
                    tmp.append(tree[idx - 1].right)

            if tree[-1].left:
                tmp.append(tree[-1].left)
            if tree[-1].right:
                tmp.append(tree[-1].right)

            tree = tmp

        return root

def build():
    """
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
    """
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
    root.right = TreeLinkNode(3)
    root.right.left = TreeLinkNode(6)
    root.right.right = TreeLinkNode(7)
    return root

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
    t = build()
    s.connect(t)
    pp(t)
    print("-----")
    t = build()
    t = s.rewrite(t)
    pp(t)
