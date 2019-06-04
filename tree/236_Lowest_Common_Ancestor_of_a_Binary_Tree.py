#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

Given a binary tree, find the lowest common ancestor (LCA)
of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes v and w
as the lowest node in T that has both v and w as descendants
(where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.
Another example is LCA of nodes 5 and 4 is 5,
since a node can be a descendant of itself according to the LCA definition.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

        dfs, bfs is not properly.
        How many states?
        iff matches, return this node.
        """

        def dfs(root):
            if root in (None, p, q):
                return root

            ln = dfs(root.left)
            rn = dfs(root.right)

            return root if ln and rn else ln if ln else rn

        return dfs(root)

def build():
    """
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
    """
    root = TreeNode(37)
    root.left = TreeNode(-34)
    root.left.left = TreeNode(-48)
    root.left.left.right = TreeNode(-100)
    root.left.left.right.shit1 = "-100-1"
    root.left.left.right.left = TreeNode(-100)
    root.left.left.right.left.shit2 = "-100-2"
    root.left.left.right.left.left = TreeNode(48)
    root.left.right = TreeNode(-54)
    root.left.right.right = TreeNode(-71)
    root.left.right.right.left = TreeNode(-22)
    root.right = TreeNode(8)
    return root, root.left.left.right, root.left.left.right.left
    return root, root.left.left.right.left, root.left.left.right
    # ---------
    root = TreeNode(3)
    root.right = TreeNode(1)
    root.left = TreeNode(5)
    root.left.right = TreeNode(2)
    root.left.left = TreeNode(6)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.right = TreeNode(8)
    root.right.left = TreeNode(0)
    return root, root.left.left, root.right.right
    return root, TreeNode(7), TreeNode(4)
    return root, TreeNode(5), TreeNode(7)


if __name__ == "__main__":
    s = Solution()
    print(s.lowestCommonAncestor(*build()))
