#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""


# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int

        BFS is better
        """

        if not root:
            return 0

        nodes = [root]
        depth = 0

        while nodes:
            depth += 1
            tmp = []

            for n in nodes:
                if not n.left and not n.right:
                    return depth

                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            nodes = tmp



def build():
   """
        3
       / \
      9  20
        /  \
       15   7
   """
   _3 = TreeNode(3)
   _9 = TreeNode(3)
   _20 = TreeNode(3)
   _15 = TreeNode(3)
   _7 = TreeNode(3)

   _3.left = _9
   _3.right = _20
   _20.left = _15
   _20.right = _7

   return _3


if __name__ == "__main__":
    s = Solution()
    print(s.minDepth(build()))
