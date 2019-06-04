#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-mode-in-binary-search-tree/description/


Given a binary search tree (BST) with duplicates,
find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than
or equal to the node's key.

The right subtree of a node contains only nodes with keys greater than
or equal to the node's key.


Both the left and right subtrees must also be binary search trees.

For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        sorry, inorder is a must...
           1
            \
             2
            /
           2

        Or:
        convert to linked list and traverse again.
        """
        from collections import Counter

        result = []

        def dfs(root):
            """
            inorder traverse
            """
            if not root:
                return

            lmin = lmax = rmin = rmax = None

            if root.left:
                lmin, lmax = dfs(root.left)

            result.append(root.val)

            if root.right:
                rmin, rmax = dfs(root.right)

            if not lmin:
                lmin = root

            if not rmax:
                rmax = root

            return lmin, rmax

        dfs(root)

        c = Counter(result)

        mx = 0
        r = []

        for t in c.most_common():
            if t[1] >= mx:
                mx = max(mx, t[1])
                r.append(t[0])

        return r


def build():
    """
   1
    \
     2
    /
   2
    """
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(1)
    root.left.right.left.right = TreeNode(2)
    return root

    root = TreeNode(6)
    root.left = TreeNode(2)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(2)
    root.left.right.right = TreeNode(6)
    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    return root

    root = TreeNode(1)
    root.right = TreeNode(2)
    return root

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    return root


if __name__ == "__main__":
    s = Solution()
    result = s.findMode(build())
    print(result)
