#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/


Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.

For example:
Given binary tree [3,9,20,null,null,15,7],


    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mmax = {"max": 0}

        def dfs(node, cnt):
            if node:
                cnt += 1
            else:
                return

            if not node.left and not node.right:
                mmax["max"] = max(mmax["max"], cnt)

            if node.left:
                dfs(node.left, cnt)

            if node.right:
                dfs(node.right, cnt)

        dfs(root, 0)

        return mmax["max"]

    def rewrite2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node:
                return 0

            return max([dfs(n) + 1 for n in (node.left, node.right) if node])
        return dfs(root)


def build():
    """
         1
       /  \
      2    3
     / \    \
    4   5    7
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(7)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


if __name__ == "__main__":
    s = Solution()
    print(s.maxDepth(build()))
    print(s.rewrite2(build()))
