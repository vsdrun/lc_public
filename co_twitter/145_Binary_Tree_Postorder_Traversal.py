#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/binary-tree-postorder-traversal/description/

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],

   1
    \
     2
    /
   3


return [3,2,1].
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []

        def dfs(node):
            if not node:
                return

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

            result.append(node.val)

        dfs(root)

        return result

    def rewrite(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def post(node):
            if not node:
                return

            if node.left:
                for n in post(node.left):
                    yield n
            if node.right:
                for n in post(node.right):
                    yield n

            yield node.val


        return [v for v in post(root)]


def build():
    """
    3
   / \
  9  20
    /  \
   15   7
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)
    return root


if __name__ == "__main__":
    s = Solution()
    print(s.postorderTraversal(build()))
    print(s.rewrite(build()))
