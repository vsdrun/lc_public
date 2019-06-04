#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/validate-binary-search-tree/description/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys
less than the node's key.

The right subtree of a node contains only nodes with keys greater
than the node's key.

Both the left and right subtrees must also be binary search trees.

Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.

Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.

"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def judge(root, lfs_mn, rhs_mx):

            if not root:
                return True

            if root.val >= rhs_mx or root.val <= lfs_mn:
                return False

            if (not root.left or judge(root.left, lfs_mn, root.val)) and \
                    (not root.right or judge(root.right, root.val, rhs_mx)):
                return True

            return False

        return judge(root, float("-inf"), float("inf"))


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
    return root


if __name__ == "__main__":
    s = Solution()
    result = s.isValidBST(build())

    print(result)
