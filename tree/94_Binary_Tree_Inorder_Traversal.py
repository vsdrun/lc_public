#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/binary-tree-inorder-traversal/description/


Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def io(node):
            if node.left:
                for l in io(node.left):
                    yield l

            yield node.val

            if node.right:
                for r in io(node.right):
                    yield r

        if not root:
            return []

        result = []

        for v in io(root):
            result.append(v)

        return result


def build():
    """
        1
       / \
      2   2
     / \ / \
       7 4  3
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.left.right = TreeNode(7)
    return root


if __name__ == "__main__":
    s = Solution()
    n = s.inorderTraversal(build())
    print(n)
