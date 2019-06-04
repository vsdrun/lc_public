#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/


Given a binary tree,
return the zigzag level order traversal of its nodes' values.
(ie, from left to right,
then right to left for the next level and alternate between).


For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        result = []

        bfs = [root]

        # BFS, level by level
        flip = -1

        while bfs:

            result.append([n.val for n in bfs if n][::-flip])
            flip = -flip

            bfs = [c for n in bfs if n for c in (n.left, n.right) if c]

        return result


def build():
    """
        1
       / \
      1   2
     / \ / \
    3  4 5  6
    """
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    return root


if __name__ == "__main__":
    s = Solution()
    print(s.zigzagLevelOrder(build()))
