#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/balanced-binary-tree/description/

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees
of every node never differ by more than 1.


Example 1:
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.


Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        DFS
        """
        def dfs(node):
            # ret: bool, max index
            if not node:
                return True, 0

            r = l = 0
            rval = lval = True

            if node.left:
                lval, l = dfs(node.left)
            if node.right:
                rval, r = dfs(node.right)

            if rval is False or lval is False or abs(l - r) > 1:
                return False, 0
            else:
                return True, 1 + l if l > r else 1 + r

        return dfs(root)[0]

def build():
    """
    3
   / \
  9  20
    /  \
   15   7
        \
         8
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)
    root.right.left = TreeNode(15)

    return root


if __name__ == "__main__":
    s = Solution()
    print(s.isBalanced(build()))
