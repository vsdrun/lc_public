#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/convert-bst-to-greater-tree/description/


Given a Binary Search Tree (BST),
convert it to a Greater Tree such that every key of the original
BST is changed to the original key plus sum of all
keys greater than the original key in BST.



Example:
Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13
Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode

        idea:
        go to the further right, and accumulate the sum.
        """
        total = [0]

        def accum(node):
            """
            go to right, accumuldate, modify, if left, then go to left.
            """
            if not node:
                return

            if node.right:
                accum(node.right)

            total[0] += node.val

            node.val = total[0]

            if node.left:
                accum(node.left)

        accum(root)
        return root

    def convertHelper(self, root):
        if not root:
            return
        self.convertHelper(root.right)
        root.val += self.cur_sum
        self.cur_sum = root.val
        self.convertHelper(root.left)


def build():
    """
      5
    /   \
   2     13
    """
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(13)
    return root


if __name__ == "__main__":
    s = Solution()
    result = s.convertBST(build())
