#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/

Given a binary tree containing digits from 0-9 only,
each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:
Input: [1,2,3]
    1
   / \
  2   3
Output: 25

Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""


# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]
        stack = []

        def sumstack():
            r = 0

            for idx, v in enumerate(stack[::-1]):
                r += v * (10**idx)

            return r

        def dfs(node):
            if not node:
                return

            stack.append(node.val)

            if not node.left and not node.right:
                result[0] += sumstack()

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

            stack.pop()

        dfs(root)

        return result[0]

def build():
    """
        4
       / \
      9   0
     / \
    5   1
    """
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    root.right = TreeNode(0)
    return root


if __name__ == "__main__":
    s = Solution()
    print(s.sumNumbers(build()))
