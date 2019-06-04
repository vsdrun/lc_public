#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-bottom-left-tree-value/description/


Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1

Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        bfs
        """

        nodes = [root]

        lst = None

        while nodes:
            lst = [n.val for n in nodes][0]

            nodes = [c for n in nodes for c in (n.left if n.left else None,
                                                n.right if n.right else None)
                     if c]

        return lst


def build():
    """
        1
       / \
      2   2
     / \ / \
       4 4  3
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
    n = s.findBottomLeftValue(build())
    print(n)
