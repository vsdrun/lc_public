#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/binary-tree-paths/

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5

All root-to-leaf paths are:
["1->2->5", "1->3"]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        stack = []
        result = []

        def dfs(root):
            if not root:
                return

            stack.append(str(root.val))

            if not root.left and not root.right:
                result.append("->".join(stack))
                stack.pop()
                return

            if root.left:
                dfs(root.left)

            if root.right:
                dfs(root.right)

            stack.pop()

        dfs(root)
        return result

    def rewrite(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        result = []
        stack = []

        def dfs(node):
            if not node:
                return

            stack.append(node)

            if not node.left and not node.right:
                result.append("->".join(str(s.val) for s in stack))
                stack.pop()
                return

            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

            stack.pop()

        dfs(root)
        return result


def build():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    return root


if __name__ == "__main__":

    s = Solution()
    print(s.binaryTreePaths(build()))
    print(s.rewrite(build()))
