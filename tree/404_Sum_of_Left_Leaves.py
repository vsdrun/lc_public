#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/sum-of-left-leaves/description/

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree,
with values 9 and 15 respectively. Return 24.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int

        need to use a TAG to differentiate left/right node.
        True as left
        False as right
        """
        ss = []

        def dfs(node, rl):
            if not node:
                return False

            lr = dfs(node.left, True)
            rr = dfs(node.right, False)
            # if rl is True, meaning Left leaf node.
            if rl and not lr and not rr:
                ss.append(node.val)

            return True

        dfs(root, False)
        return sum(ss)


def build():
    """
    3
   / \
  9  20
 /  /  \
8  15   7
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = TreeNode(8)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)
    return root
    return None


if __name__ == "__main__":
    s = Solution()
    print(s.sumOfLeftLeaves(build()))
