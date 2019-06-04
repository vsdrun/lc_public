#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

Given a Binary Search Tree and a target number,
return true if there exist two elements in the BST such
that their sum is equal to the given target.


Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True

Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        def find(root, v):
            if root.val == v:
                return True

            if v < root.val and root.left:
                return find(root.left, v)
            elif root.right:
                return find(root.right, v)

            return False

        bfs_list = [root]

        while bfs_list:
            node = bfs_list.pop(0)
            remain = k - node.val

            if remain != node.val and find(root, remain):
                return True

            if node.left:
                bfs_list.append(node.left)
            if node.right:
                bfs_list.append(node.right)

        return False


def build():
    """
    9
   / \
  3  20
 /  /  \
2  15   22
    """
    root = TreeNode(1)
    return root, 2

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    return root, 4

    root = TreeNode(9)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.right = TreeNode(20)
    root.right.right = TreeNode(22)
    root.right.left = TreeNode(15)
    return root, 12


if __name__ == "__main__":
    s = Solution()
    print(s.findTarget(*build()))
