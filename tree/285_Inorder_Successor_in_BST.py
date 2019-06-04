#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/inorder-successor-in-bst/description/


Given a binary search tree and a node in it,
find the in-order successor of that node in the BST.


Note: If the given node has no in-order successor in the tree, return null.
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if p.val < root.val:
            return self.rewrite(root.left, p) or root
        else:  # >=
            return self.rewrite(root.right, p)


def build():
    """
        5
       / \
      3   7
     / \
    2   4
    """
    root = TreeNode(5)
    root.right = TreeNode(7)
    root.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.left = TreeNode(2)
    return root, 3


if __name__ == "__main__":
    s = Solution()
    #  result = s.inorderSuccessor(build())
    #  print(result)

    result = s.rewrite(*build())
    print(result.val)
