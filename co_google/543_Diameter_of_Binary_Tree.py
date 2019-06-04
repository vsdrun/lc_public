#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/diameter-of-binary-tree/

Given a binary tree, you need to compute the length of the diameter
of the tree.

The diameter of a binary tree is the length of the longest path
between any two nodes in a tree.

This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

注意:
    除了單一node的累積值，
    還有要考慮此單一node下的diameter可能已經是最大!
    例如node A下的左到右已經是MAX.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        1. save deepest length
        2. save max diff from left/right.
        """

        def run(r):
            ld = 0
            rd = 0
            llm = 0
            rlm = 0
            lmax = 0

            if r.left:
                ld += 1
                d, llm = run(r.left)
                ld = ld + d

            if r.right:
                rd += 1
                d, rlm = run(r.right)
                rd = rd + d

            lmax = max(llm, rlm, rd + ld)

            return rd if rd > ld else ld, lmax

        _, cm = run(root) if root else (0, 0)

        return cm

    def rewrite(self, root):
        """
        :type root: TreeNode
        :rtype: int
        1. save deepest length
        2. save max diff from left/right.
        3. 往上傳時 + 1 as path.
        """
        curmax = [0]

        def dfs(node):
            """
            curmax = max(curmax, diff(left, right))
            :ret: int, length
            """
            if not node:
                return 0

            left = dfs(node.left)
            right= dfs(node.right)

            curmax[0] = max(curmax[0], left + right)

            return left + 1 if left > right else right + 1

        dfs(root)
        return curmax[0]

def build():
    """
          1
         / \
        2   3
       / \
      4   5
    """
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.left.left = TreeNode(4)
    r.left.right = TreeNode(5)

    r.right = TreeNode(3)

    return r
    return TreeNode(3)


if __name__ == "__main__":

    print(Solution().diameterOfBinaryTree(build()))
    print(Solution().rewrite(build()))
