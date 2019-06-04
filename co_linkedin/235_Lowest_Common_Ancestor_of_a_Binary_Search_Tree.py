#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

Given a binary search tree (BST),
find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes v and w as the
lowest node in T that has both v and w as descendants
(where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5

For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.

Another example is LCA of nodes 2 and 4 is 2,
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
        """

        r = root

        while r:
            if p.val > r.val and q.val > r.val:
                r = r.right
            elif p.val < r.val and q.val < r.val:
                r = r.left
            else:
                return r


def build():
    """
        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
    """
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.right.right = TreeNode(9)
    root.right.left = TreeNode(7)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    return None, root.left, root.left.right
    return root, root.left, root.left.right


if __name__ == "__main__":
    s = Solution()
    r = s.lowestCommonAncestor(*build())
    print(r.val if r else None)
