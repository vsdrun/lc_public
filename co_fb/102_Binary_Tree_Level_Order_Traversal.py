#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

想到 BFS.
一次一層
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []

        bfs = [root]

        while bfs:
            tmp_r = [node.val for node in bfs if node]

            if tmp_r:
                result.append(tmp_r)

            tmp_bfs = []

            for node in bfs:
                if node:
                    tmp_bfs.append(node.left)
                    tmp_bfs.append(node.right)

            bfs = tmp_bfs

        return result

    def rewrite(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        nodes = [root]
        result = []

        while nodes:
            values = [n.val for n in nodes]
            result.append(values)

            nodes = [i for n in nodes for i in (n.left, n.right) if i]

        return result

    def rewrite2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        def bfs(node):
            tree = [node]

            while tree:
                result.append([t.val for t in tree])

                tree = \
                    [t for n in tree if n \
                        for t in (n.left, n.right) if t]


        bfs(root)

        return result


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
    print(s.levelOrder(build()))
    print(s.rewrite(build()))
    print(s.rewrite2(build()))
