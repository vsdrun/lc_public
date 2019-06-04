#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/trim-a-binary-search-tree/description/


Given a binary search tree and the lowest and highest boundaries as
L and R, trim the tree so that all its elements lies in [L, R] (R >= L).
You might need to change the root of the tree,
so the result should return the new root of the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1
"""


# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        def trim(node, L, R):
            """
            do one thing, trim.
            :ret: node
            """
            if not node:
                return

            if node.val > R:
                return trim(node.left, L, R)
            if node.val < L:
                return trim(node.right, L, R)

            node.left = trim(node.left, L, R)
            node.right = trim(node.right, L, R)
            return node


        return trim(root, L, R)

def build():
    return 1000021
    return 1234567654321
    return 100001
    return 1


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(build()))
