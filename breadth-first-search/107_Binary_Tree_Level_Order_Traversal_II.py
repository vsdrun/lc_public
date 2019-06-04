#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

Given a binary tree, return the bottom-up level order traversal of its
nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        def dfs(nodes):
            if not nodes:
                return

            next = []

            for n in nodes:
                if n.left:
                    next.append(n.left)
                if n.right:
                    next.append(n.right)

            dfs(next)

            result.append([n.val for n in nodes if n])

        if root:
            dfs([root])
        return result

    def rewrite(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        nodes = [root]

        while nodes:
            next = []
            for n in nodes:
                if n.left:
                    next.append(n.left)
                if n.right:
                    next.append(n.right)
            result.append([n.val for n in nodes])
            nodes = next

        return result[::-1]

def build():
    """
    3
   / \
  9  20
    /  \
   15   7
    """
    _3 = TreeNode(3)
    _9 = TreeNode(9)
    _20 = TreeNode(20)
    _15 = TreeNode(15)
    _7 = TreeNode(7)
    _3.left = _9
    _3.right = _20
    _20.left = _15
    _20.right = _7
    return _3


if __name__ == "__main__":
    s = Solution()
    print(s.levelOrderBottom(build()))
    print(s.rewrite(build()))
