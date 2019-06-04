#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/path-sum/description/


Given a binary tree and a sum,
determine if the tree has a root-to-leaf path such that
adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        using minus
        """

        def dfs(node, s):
            """
            :ret: true, false
            """

            if not node:
                return False

            if not node.left and not node.right and s == node.val:
                return True

            lv = rv = False

            if node.left:
                lv = dfs(node.left, s - node.val)

            if node.right:
                rv = dfs(node.right, s - node.val)

            return lv or rv

        return dfs(root, s)

    def rewrite(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        using minus!
        """
        def dfs(node, s):
            if not node:
                return False

            if not node.left and not node.right and s-node.val == 0:
                return True

            if dfs(node.left, s - node.val):
                return True

            if dfs(node.right, s - node.val):
                return True

            return False

        return dfs(root, s)


def build():
    """
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    return root, 7


if __name__ == "__main__":
    s = Solution()
    print(s.hasPathSum(*build()))
    print(s.rewrite(*build()))
