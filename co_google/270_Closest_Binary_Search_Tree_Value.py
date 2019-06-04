#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/closest-binary-search-tree-value/description/


Given a non-empty binary search tree and a target value,
find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        prev = [None, float("inf")]  # value, abs diff

        while root:
            tmp = root

            if root.val < target:
                root = root.right
            else:
                root = root.left

            mval = abs(target - tmp.val)

            if prev[1] > mval:
                prev[0] = tmp.val
                prev[1] = mval

        return prev[0]


def build():
    """
   1
    \
     2
    """

    root = TreeNode(1)
    root.right = TreeNode(2)
    return root, 3.428571

    root = TreeNode(6)
    root.left = TreeNode(2)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    return root, 5


if __name__ == "__main__":
    s = Solution()
    result = s.closestValue(*build())
    print(result)
